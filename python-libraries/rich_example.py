import csv
from rich.console import Console
from rich.table import Table
import os

# Initialize the console
console = Console()

# Create a list to store initial and added song data
song_data = [
    ["2020", "Sanctuary", "Joji"],
    ["1994", "All I Want for Christmas Is You", "Mariah Carey"],
    ["2019", "Bad Guy", "Billie Eilish"],
    ["2021", "Montero (Call Me by Your Name)", "Lil Nas X"]
]

# Create the table for favorite songs (for displaying purposes only)
table = Table(title="Favorite Songs")
table.add_column("Release Year", style="cyan", no_wrap=True)
table.add_column("Song Title", style="magenta")
table.add_column("Artist", justify="right")

# Add the initial songs to the table for display
for song in song_data:
    table.add_row(song[0], song[1], song[2])

# Function to collect user input and store it in the song_data list
def add_song():
    """Collects user input and confirms before adding the song to the list."""
    while True:
        console.print("\n[bold cyan]Now I want you to enter your favorite songs:[/bold cyan]")
        
        # Collect user input for favorite songs
        song_title = input("Enter the title of the song: ")
        release_year = input("Enter the release year of the song: ")
        artist = input("Enter the artist: ")

        # Display entered data for confirmation
        console.print(f"\n[bold yellow]You entered:[/bold yellow]")
        console.print(f"[bold]Song Title:[/bold] {song_title}")
        console.print(f"[bold]Release Year:[/bold] {release_year}")
        console.print(f"[bold]Artist:[/bold] {artist}")
        
        confirmation = input("\nIs this information correct? (y/n): ").strip().lower()
        if confirmation == 'y':
            # Add the song to the table (for display) and to the song_data list (for saving)
            table.add_row(release_year, song_title, artist)
            song_data.append([release_year, song_title, artist])
            console.print("[green]Data added![/green]")
            break
        else:
            console.print("[red]Please re-enter the data.[/red]")

# Function to save the song data to a CSV file
def save_data_to_file(file_path):
    """Save the song data to a CSV file."""
    with open(file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # Write the header
        writer.writerow(["Release Year", "Song Title", "Artist"])
        # Write each row of song data
        writer.writerows(song_data)

# Main function to add songs and save them to a CSV file
def main():
    # Print the initial table with pre-existing songs
    console.print("\n[bold cyan]Initial list of songs:[/bold cyan]")
    console.print(table)
    
    # Ask the user how many additional songs they want to enter
    console.print("\n[bold cyan]How many additional songs would you like to enter?[/bold cyan]")
    num_songs = int(input("Enter the number of songs: "))
    
    for _ in range(num_songs):
        add_song()
    
    # Print the updated table with all entries
    console.print("\n[bold cyan]Updated list of songs:[/bold cyan]")
    console.print(table)
    
    # Confirm before saving to file
    save_confirmation = input("\nDo you want to save this data to a CSV file? (y/n): ").strip().lower()
    if save_confirmation == 'y':
        file_path = os.path.join(os.getcwd(), "favorite_songs.csv")
        save_data_to_file(file_path)
        console.print(f"\n[green]Data has been saved to {file_path}[/green]")
    else:
        console.print("[red]Data was not saved.[/red]")

# Run the main program
if __name__ == "__main__":
    main()
