# Use a lightweight web server image
FROM nginx:alpine

# Install envsubst for substituting environment variables in the HTML file
RUN apk add --no-cache gettext

# Copy the HTML template file into the container
COPY index.html.template /usr/share/nginx/html/index.html.template

# Substitute the environment variable and save it as index.html
CMD envsubst '${API_URL}' < /usr/share/nginx/html/index.html.template > /usr/share/nginx/html/index.html && nginx -g 'daemon off;'
