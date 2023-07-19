import requests
import json
import os
import os
import platform

@staticmethod
def find(key, name):
    url = "https://api.notion.com/v1/search"
    payload = {
        "filter": {
            "value": "database",
            "property": "object"
        },
        "page_size": 100,
        "query": name
    }
    headers = {
        "Authorization": f"Bearer {key}",
        "accept": "application/json",
        "Notion-Version": "2022-06-28",
        "content-type": "application/json"
    }
    response = requests.post(url, json=payload, headers=headers)
    response_json = response.json()
    if response: return True, response_json
    else: return False, response

@staticmethod
def set_environment_variable(name, value):
    system = platform.system()
    scriptDir = os.path.dirname(os.path.realpath(__file__))
    if system == "Windows":
        if not os.path.exists(os.path.join(scriptDir, 'set_env.bat')): 
            with open(os.path.join(scriptDir, 'set_env.bat'), 'w') as f: f.write('')
        with open(os.path.join(scriptDir, 'set_env.bat'), 'a') as f: 
            f.write(f'setx {name} "{value}"\n')
        print(f'\nWrote commands to set environment variables to {os.path.join(scriptDir, "set_env.bat")}.')
        print(f'Please run {os.path.join(scriptDir, "set_env.bat")} as Administrator to set the variables.')
    else:
        if not os.path.exists(os.path.join(scriptDir, 'set_env.sh')): 
            with open(os.path.join(scriptDir, 'set_env.sh'), 'w') as f: f.write('')
        with open(os.path.join(scriptDir, 'set_env.sh'), 'a') as f: 
            f.write(f'export {name}={value}\n')
        subprocess.call(['chmod', '+x', os.path.join(scriptDir, 'set_env.sh')])
        print(f'\nWrote commands to set environment variables to {os.path.join(scriptDir, "set_env.sh")}.')
        print(f'To set these environment variables in your shell, use the command: `source {os.path.join(scriptDir, "set_env.sh")}`')

if __name__ == '__main__':
    input('\nDuplicate the Error Log Notion template:\nhttps://flytlabs.notion.site/255a9161424c473a91c8c2d36678a53b?v=b46290c3087f44b58d93e60d090976e9&pvs=4\n[Enter] to continue...')
    input('\nGet Notion API key:\nhttps://www.notion.so/my-integrations\n[Enter] to continue...')
    while True:
        apiKey = input('\nNotion API Key\n(Ensure the integration is added within the page settings): ')
        pageName = input('\nCase-sensitive duplicated page name: ')
        success,data = find(apiKey, pageName)
        if success: print(f'\nNotion Page ID: {data["results"][0]["id"]}')
        else: 
            print(f'Could not find page! Response:\n\n{data}\n')
            try: print(f'{json.dumps(data.json(),indent=4)}\n')
            except: print(f'{data.content}\n')
            print('Please try again to complete the setup.')
            continue
        scriptDir = os.path.dirname(os.path.realpath(__file__))
        set_environment_variable("NOTION_TOKEN", apiKey)
        set_environment_variable("NOTION_DB_ID", data["results"][0]["id"])
        done = input('[Enter] to complete...')
        quit()
        