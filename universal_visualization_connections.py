# Tableau REST API (Publishing to Tableau Server)
def test_tableau():
    import requests
    tableau_url = 'https://your-tableau-server/api/3.18'
    username = 'your_username'
    password = 'your_password'
    payload = {
        "credentials": {
            "name": username,
            "password": password,
            "site": {"contentUrl": ""}
        }
    }
    response = requests.post(f"{tableau_url}/auth/signin", json=payload)
    print("Tableau connection works:", response.status_code == 200)

# Power BI API (Sample auth, requires setup and app registration)
def test_powerbi():
    import requests
    # Substitute with valid Azure AD access token and workspace ID
    token = 'your_access_token'
    workspace_id = 'your_workspace_id'
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"https://api.powerbi.com/v1.0/myorg/groups/{workspace_id}/reports", headers=headers)
    print("Power BI connection works:", response.status_code == 200)

# Plotly Dash (Simple local startup)
def test_dash():
    import dash
    from dash import html
    app = dash.Dash(__name__)
    app.layout = html.Div(children=[html.H1('Dash Connection Works')])
    # app.run_server(debug=True) # Uncomment to start app
    print("Dash code configured (uncomment to run server).")

# Google Data Studio (Looker Studio, sample embed check)
def test_data_studio():
    # Typically Data Studio dashboards are embedded via iframes/URLs
    dashboard_url = "https://datastudio.google.com/reporting/your-report-id"
    import requests
    response = requests.get(dashboard_url)
    print("Google Data Studio report embed reachable:", response.status_code == 200)

if __name__ == "__main__":
    # Uncomment based on your accounts/environment.
    # test_tableau()
    # test_powerbi()
    test_dash()
    # test_data_studio()
