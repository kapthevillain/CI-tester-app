import os, json



def test_index(app, client):
    res = client.get('/')
    assert res.status_code == 200
    # expected = {'hello': 'world'}
    expectedGreeting = {'Port':os.environ['FLASK_PORT'], 'Environment':os.environ['ENV'], '👋':'🌎'}
    assert len(expectedGreeting) == len(json.loads(res.get_data(as_text=True)))
    assert expectedGreeting == json.loads(res.get_data(as_text=True))
