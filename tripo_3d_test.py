import requests
import base64
import json
import time

# Function to encode image to base64
def encode_image(file_path):
    with open(file_path, 'rb') as file:
        return base64.b64encode(file.read()).decode('utf-8')

# Function to make API request to convert image to model
def image_to_model(api_key, image_data):
    url = "https://api.tripo3d.ai/v2/openapi/task"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    data = {
        "type": "image_to_model",
        "file": {
            "type": "jpeg",  # Correct MIME type for JPEG
            "data": image_data
        }
    }
    
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()  # Return the full JSON response
    else:
        raise Exception("Failed to post data: " + response.text)

# Function to check task status
def check_task_status(api_key, task_id):
    url = f"https://api.tripo3d.ai/v2/openapi/task/{task_id}"
    headers = {
        "Authorization": f"Bearer {api_key}"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()  # Return the full JSON response
    else:
        raise Exception("Failed to get task status: " + response.text)

# Main code execution
api_key = ""
image_data = encode_image('./car.jpg')

try:
    # Make the POST request and print the response
    post_response = image_to_model(api_key, image_data)
    task_id = post_response['data']['task_id']
    #wait 15 seconds
    time.sleep(15)
    # Use the task ID to make the GET request and print the response
    get_response = check_task_status(api_key, task_id)
    print(json.dumps(get_response, indent=4))

except Exception as e:
    print(e)
