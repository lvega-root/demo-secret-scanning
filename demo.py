import yaml

def load_credentials(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

def main():
    credentials = load_credentials('credentials.yml')
   
    aws_access_key_id = credentials['aws']['access_key_id']
    aws_secret_access_key = credentials['aws']['secret_access_key']
    github_pat = credentials['github']['personal_access_token']
   
    print(f"AWS Access Key ID: {aws_access_key_id}")
    print(f"AWS Secret Access Key: {aws_secret_access_key}")
    print(f"GitHub Personal Access Token: {github_pat}")

if __name__ == "__main__":
    main()
