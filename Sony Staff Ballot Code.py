import random

# List of staff members
staff_list = ["Jason Wise", "Japekam Dang", "Tony Lin", "Jason Anto", "James Guo"]

# Items in each category
tv_prizes = ["XR55A95L", "XR77A80L", "XR85X90K"]
audio_prizes = ["WH1000XM4B", "WH1000XM5B", "WH1000XM5L", "WH1000XM5B", "WH1000XM4S", "WH1000XM5S", "WH1000XM5L"]
projector_prizes = ["Projector1", "Projector2", "Projector3"]

# Dictionary to track the winners for each category
prize_winners = {
    "TVs": {},
    "Audio": {},
    "Projectors": {}
}

# Function to pick winners for a category
def select_winners(prizes, category):
    available_staff = staff_list[:]
    for prize in prizes:
        if not available_staff:
            print(f"Not enough staff members to award all {category} prizes.")
            break
        winner = random.choice(available_staff)
        prize_winners[category][winner] = prize
        available_staff.remove(winner)

# Select winners for each category
select_winners(tv_prizes, "TVs")
select_winners(audio_prizes, "Audio")
select_winners(projector_prizes, "Projectors")

# Print the results
print("Prize Winners:")
for category, category_winners in prize_winners.items():
    print(f"\n{category}:")
    for staff, prize in category_winners.items():
        print(f"{staff} won {prize}")

# Function to check if a staff member has already won in a category
def has_won(category, staff_member):
    return staff_member in prize_winners[category]

# Example check
print("\nCheck if a staff member has won in a category:")
print(f"Jason Wise won a TV: {has_won('TVs', 'Jason Wise')}")
print(f"Japekam Dang won an Audio prize: {has_won('Audio', 'Japekam Dang')}")
