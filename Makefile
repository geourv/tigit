LOCAL_CORE ?= /opt/unaltraweb
LOCAL_GEMFILE := tmp/Gemfile.local
MCP_IMAGE ?= ghcr.io/dosquartsdedocs/unaltraweb-mcp:0.3.0
UNALTRAWEB_CAPTURE_RUNTIME := 1
LOCAL_UID ?= $(shell id -u)
LOCAL_GID ?= $(shell id -g)
PORT ?= 4000
BASEURL ?= /tigit
START_PATH ?= /ca/
CONTAINER ?= unaltraweb-site-$(shell printf '%s' '$(CURDIR)' | cksum | cut -d' ' -f1)
PLAYWRIGHT_IMAGE ?= mcr.microsoft.com/playwright:v1.56.1-noble

.PHONY: local-gemfile site-check-native build-native serve-capture-native serve-native test-native build serve test listing-smoke down clean

local-gemfile:
	@mkdir -p tmp
	@printf '%s\n' 'source "https://rubygems.org"' '' 'group :jekyll_plugins do' '  gem "unaltraweb", path: "$(LOCAL_CORE)"' 'end' > $(LOCAL_GEMFILE)

site-check-native:
	@unaltraweb-mcp --project "$(CURDIR)" mcp site-check >/dev/null

build-native: local-gemfile site-check-native
	@BUNDLE_GEMFILE=$(LOCAL_GEMFILE) bundle lock --local
	@BUNDLE_GEMFILE=$(LOCAL_GEMFILE) bundle check
	@BUNDLE_GEMFILE=$(LOCAL_GEMFILE) bundle exec jekyll build --config $(LOCAL_CORE)/_config.yml,_config.yml --disable-disk-cache

serve-capture-native: local-gemfile
	@BUNDLE_GEMFILE=$(LOCAL_GEMFILE) bundle lock --local
	@BUNDLE_GEMFILE=$(LOCAL_GEMFILE) bundle check
	@BUNDLE_GEMFILE=$(LOCAL_GEMFILE) bundle exec jekyll serve --config $(LOCAL_CORE)/_config.yml,_config.yml --host $${HOST:-0.0.0.0} --port $${PORT:-4000} --disable-disk-cache

serve-native: site-check-native serve-capture-native

test-native: build-native
	@unaltraweb-mcp --project "$(CURDIR)" mcp html-audit >/dev/null

build:
	@docker run --rm --user "$(LOCAL_UID):$(LOCAL_GID)" -e HOME=/tmp -v "$(CURDIR):/workspace" -w /workspace --entrypoint make "$(MCP_IMAGE)" --silent build-native LOCAL_CORE=/opt/unaltraweb

serve:
	@docker run --rm --name "$(CONTAINER)" --user "$(LOCAL_UID):$(LOCAL_GID)" -e HOME=/tmp -p "$(PORT):$(PORT)" -v "$(CURDIR):/workspace" -w /workspace --entrypoint make "$(MCP_IMAGE)" --silent serve-native LOCAL_CORE=/opt/unaltraweb HOST=0.0.0.0 PORT="$(PORT)"

test:
	@docker run --rm --user "$(LOCAL_UID):$(LOCAL_GID)" -e HOME=/tmp -v "$(CURDIR):/workspace" -w /workspace --entrypoint make "$(MCP_IMAGE)" --silent test-native LOCAL_CORE=/opt/unaltraweb
	@$(MAKE) --silent listing-smoke

listing-smoke:
	@mkdir -p tmp/render-smoke
	@set -eu; \
	container="$(CONTAINER)-browser"; \
	docker rm -f "$$container" >/dev/null 2>&1 || true; \
	docker run -d --rm --name "$$container" --user "$(LOCAL_UID):$(LOCAL_GID)" -e HOME=/tmp --network host -v "$(CURDIR):/workspace" -w /workspace --entrypoint bash "$(MCP_IMAGE)" -lc 'BUNDLE_GEMFILE=tmp/Gemfile.local bundle exec jekyll serve --config /opt/unaltraweb/_config.yml,_config.yml --host 127.0.0.1 --port $(PORT) --skip-initial-build --disable-disk-cache' >/dev/null; \
	cleanup() { docker stop "$$container" >/dev/null 2>&1 || true; }; \
	trap cleanup EXIT; \
	ready=0; \
	for attempt in $$(seq 1 60); do \
		if curl -fsS "http://127.0.0.1:$(PORT)$(BASEURL)$(START_PATH)" >/dev/null 2>&1; then ready=1; break; fi; \
		sleep 1; \
	done; \
	if test "$$ready" != 1; then docker logs "$$container" >&2; exit 1; fi; \
	docker run --rm --user "$(LOCAL_UID):$(LOCAL_GID)" --network host --ipc=host -e HOME=/tmp -e BASE_URL="http://127.0.0.1:$(PORT)$(BASEURL)" -e RENDER_OUT=/work/tmp/render-smoke -e SITE_PROFILE=unaltremanual -v "$(CURDIR):/work" -w /tmp "$(PLAYWRIGHT_IMAGE)" bash -lc 'mkdir playwright && cd playwright && npm init -y >/dev/null && npm install --no-save --no-package-lock @playwright/test@1.56.1 >/dev/null && cp /work/tests/render-smoke.spec.mjs . && npx playwright test render-smoke.spec.mjs --browser=chromium --output=/work/tmp/render-smoke/test-results --grep "TIGIT inherits manual presentation" --workers=1 $(PLAYWRIGHT_ARGS)'

down:
	@container="$$(docker ps -aq --filter "name=^/$(CONTAINER)$$")"; if test -n "$$container"; then docker rm -f "$$container" >/dev/null; fi
	@container="$$(docker ps -aq --filter "name=^/$(CONTAINER)-browser$$")"; if test -n "$$container"; then docker rm -f "$$container" >/dev/null; fi

clean:
	@rm -rf _site tmp .jekyll-cache
