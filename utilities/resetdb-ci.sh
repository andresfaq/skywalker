# Reiniciador de la base de datos
# Reemplazen el nombre de usuario
# Ejecuten haciendo [sh resetdb.sh] en consola
sudo -u ubuntu psql -c 'DROP DATABASE circleci;'
sudo -u ubuntu psql -c 'CREATE DATABASE circleci WITH OWNER ubuntu;'
sudo -u ubuntu psql -c 'GRANT ALL PRIVILEGES ON DATABASE skywalker TO ubuntu;'
