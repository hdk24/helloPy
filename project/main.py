from project import app

# host 0.0.0.0 public ip, to access in device use ip address
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
