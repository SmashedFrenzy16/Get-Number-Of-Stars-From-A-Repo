from github import Github

g_cred = Github("<Paste Your Token Here>")

f_repo = input("Enter repository name to see its stars (eg. User/Repo): ")

repo = g_cred.get_repo(f_repo)

print(repo.stargazers_count)
