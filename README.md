# Add User to Organization with CSV

This script is used to add members to Labelbox org with a csv sheet.

The script is set up to use arguments inside your CLI to customize how you want to add users. (add them to org, add them to just a project, headers, what role)

To start you need to add your api key from your workspace to the `api_key.py` file.

## Add to Organization

The script defaults to just add the user to your organization with a default role of `LABELER`.

`python add_users.py <csv file path>`

To change the default role you can use the `--role` or `-r` flag.

`python add_users.py <csv file path> -r ADMIN`

## Add to Project

You can also change the script to add the users to the specified project id with the `--basis` or `-b` flag.

`python add_users.py <csv file bath> -b project`

You can also adjust the role given like you can with adding to just your organization.

To change the default role you can use the `--role` or `-r` flag.

`python add_users.py <csv file path> -b project -r ADMIN`

## CSV Headers

By default the headers that are used for the user email and the project id are `Email` and `Project ID` the example.csv shows the headers. If your headers and named something different you can modify which header the tool is using with the `--email-header` or `-eh` and the `--project-header` or `-ph` flags.

`python add_users.py <csv file path> -eh <email header column on csv> -ph <project header column on csv>`

## Help

For help with this script type the following in your CLI. This will break down each of the flags.

`python add_users.py -h`