file_loco = 'fileprocessor.input'

with open(file_loco, 'r') as file:
    lines = file.readlines()

    print("Printing out User Data:\n")

    commented_line = False
for line in lines:
    line = line.strip()
    if line.startswith('#'):
         commented_line = True
         continue

    user_data = line.split(':')
    if len(user_data)< 4:
        continue
    username = user_data[0]
    password = user_data[1]
    userid = user_data[2]
    groupid = user_data[3]


    print(f"The user {username} has a password of {password} and has userid {userid} and groupid {groupid}")
if commented_line == True:
    print("User4 is skipped because it starts with a hashtag (is commented out)")
print("\nEnd of User Data")


