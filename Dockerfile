# Use the official Prometheus image as the base image
FROM prom/prometheus:latest

# Add Prometheus configuration file
# COPY ./p.yml prometheus.yml
# RUN mkdir -p prometheus/prometheus-data
# Copy the custom data folder

# Ensure the custom data folder has the correct permissions
USER root
RUN mkdir -p prometheus-data && chown -R root:root prometheus-data
COPY ./downloaded_folder/ prometheus-data

# Switch back to the Prometheus user

CMD ["--storage.tsdb.path=prometheus-data"]
