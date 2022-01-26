# make script executable & run service
chmod +x app.py
./app.py &
# test the server 
curl -i localhost:5000/
curl -i localhost:5000/hello/
curl -i localhost:5000/hello/Simon
