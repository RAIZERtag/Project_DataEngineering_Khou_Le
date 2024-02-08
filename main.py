from visualization import create_dashboard

if __name__ == '__main__':
    app = create_dashboard()
    app.run_server(host='127.0.0.1',debug=False, port=8050)
