# Project-specific R packages for TIGIT manual computations.
# The base image builds on rocker/geospatial and already includes the common
# spatial stack used for ggplot2-based maps and geospatial figures.
# Add install.packages(...) calls here when a source needs packages beyond it.
#
# For demo graphics in the manual chapters:
# - boxplot:    base R graphics, no extra package needed
# - alluvial:   ggalluvial required below (Titanic dataset ships with R base)
install.packages("ggalluvial", repos = "https://cloud.r-project.org")