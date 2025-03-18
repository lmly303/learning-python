import json


# function to load data from txt file to json format 
def load_data():
    try:
        with open('youtube_manager.txt', 'r') as file:
            test = json.load(file)
            return test
    except FileNotFoundError:
        return []
    
# function to save the changes in the txt file
def save_data_helper(videos):
    with open('youtube_manager.txt', 'w') as file:
        json.dump(videos, file)


def list_all_videos(videos):
    print("*"*70)
    print("\n")
    for index,video in enumerate(videos, start=1):
        print(f"{index}. {video['name']}, Duration: {video['duration']}")
    print("\n")
    print("*"*70)

def add_new_video(videos):
    name = input("Enter the name of the video: ")
    duration = input("Enter the duration: ")
    videos.append({'name':name, 'duration': duration})
    save_data_helper(videos)

def update_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the index you want to update: "))
    if 1<= index <= len(videos):
        name = input("Enter the name of the video: ")
        duration = input("Enter the duration: ")
        videos[index-1] = {'name':name, 'duration': duration}
        save_data_helper(videos)
        print("---   Updates executed successfully!   ---")
    else:
        print("Enter a valid index number!")
        update_video(videos)

def delete_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the index you want to delete: "))
    if 1<= index <= len(videos):
        del videos[index-1]
        save_data_helper(videos)
        print("---   Video deleted successfully!   ---")
    else:
        print("Enter a valid index number!")
        update_video(videos)


def main():
    videos = load_data()
    while True:
        print("\n")
        print(f"Youtuber Manager | Choose an option from below list :")
        print(f"1. List all youtube videos")
        print("2. Add a youtube video ")
        print("3. Update a youtube video details ")
        print("4. Delete a youtube video ")
        print("5. Exit the app ")
        choice = input("Enter your choice: ")

        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_new_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case _:
                print("Invalid choice!")

if __name__ == "__main__":
    main()