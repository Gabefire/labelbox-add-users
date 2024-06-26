import argparse
import csv
import labelbox as lb
from api_key import API_KEY

client = lb.Client(API_KEY)

def add_org(user_email, role):
    roles = client.get_roles()
    organization = client.get_organization()
    organization.invite_user(email=user_email, role=roles[role])
    
def add_project(user_email, project_id, role):
    roles = client.get_roles()

    organization = client.get_organization()
    project = client.get_project(project_id)
    
    project_role = lb.ProjectRole(project, roles[role])
    organization.invite_user(email=user_email, project_roles=[project_role], role=roles["NONE"])
    
def main(args_dict: dict):
    with open(args_dict["filename"], newline="") as csvfile:
        csvreader = list(csv.reader(csvfile))
        headers:list = csvreader[0]
        
        if args_dict["project_header"] not in headers:
            raise Exception(f"{args_dict['project_header']} not in csv headers: {headers}")
        
        elif args_dict["email_header"] not in headers:
            raise Exception(f"{args_dict['email_header']} not in csv headers: {headers}")
        
        if args_dict["project_header"] not in headers:
            raise Exception(f"not in csv headers: {headers}")
        
        elif args_dict["email_header"] not in headers:
            raise Exception(f" not in csv headers: {headers}")
        
        for row in csvreader[1:]:
            if args_dict["basis"] == "organization":
                add_org(row[headers.index(args_dict["email_header"])], args_dict["role"])
                
            elif args_dict["basis"] == "project":
                add_project(row[headers.index(args_dict["email_header"])], row[headers.index(args_dict["project_header"])], args_dict["role"])
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
    prog="Add Users to Organization",
    description="Script to add users to Labelbox organization with a CSV file")
    
    parser.add_argument("filename")
    parser.add_argument("-b", "--basis", help="Should users be added as a organization basis or project basis?", default="organization", choices=["organization", "project"])
    parser.add_argument("-r", "--role", help="What role should users have? (all caps defaults to Labeler)", default="LABELER")
    parser.add_argument("-ph", "--project-header", help="Project ID header name on csv", default="Project ID")
    parser.add_argument("-eh", "--email-header", help="Email header name on csv", default="Email")
    
    main(vars(parser.parse_args()))
    