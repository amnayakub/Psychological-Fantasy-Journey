import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time


def print_slowly(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.00)
    print()


def get_choice(prompt, options):
    while True:
        choice = input(prompt).strip()
        if choice in options:
            return choice
        print("❌ Invalid choice. Please try again.")


print_slowly("🧠 Auralith: A Realm Shaped by You")
print_slowly(
    "\nThe air hums with latent magic as you find yourself standing before a gate made of swirling starlight.")
print_slowly(
    "A voice echoes from nowhere and everywhere: 'What name does your soul whisper?'")
name = input("> ").strip()

print_slowly(f"\nWelcome, {name}. Your mind shapes this world.")
print_slowly(f"\nDear {name},")
print_slowly(
    "You awaken not in a world of stone and sky—but one shaped by your thoughts, beliefs, and desires.")
print_slowly("Here, choices reveal the inner you. Let us begin...")

stats = {
    'Openness': {
        'score': 50,
        'subtraits': ['Imagination', 'Artistic Interest', 'Emotionality', 'Adventurousness', 'Intellect']
    },
    'Conscientiousness': {
        'score': 50,
        'subtraits': ['Self-Efficacy', 'Orderliness', 'Dutifulness', 'Achievement-Striving', 'Self-Discipline']
    },
    'Extraversion': {
        'score': 50,
        'subtraits': ['Friendliness', 'Gregariousness', 'Assertiveness', 'Activity Level', 'Excitement-Seeking']
    },
    'Agreeableness': {
        'score': 50,
        'subtraits': ['Trust', 'Morality', 'Altruism', 'Cooperation', 'Modesty']
    },
    'Neuroticism': {
        'score': 50,
        'subtraits': ['Anxiety', 'Anger', 'Depression', 'Self-Consciousness', 'Vulnerability']
    }
}

# ✨ Scene 1: The Luminescent Letter


def scene_letter():
    print("\n" + "="*50)
    print("🌟 THE LUMINESCENT LETTER 🌟")
    print("="*50)
    print_slowly(
        "\nA pulsing envelope materializes before you, its parchment shifting between colors.")
    print_slowly(
        "The wax seal bears your initials—though you've never owned such a seal.")
    print_slowly(
        "As you touch it, whispers flood your mind showing glimpses of Auralith:")
    print_slowly(
        "- A library where books rewrite themselves based on readers' thoughts")
    print_slowly(
        "- A bridge that extends only when someone takes a leap of faith")
    print_slowly(
        "- A mirror that reflects not your face, but your current emotional state")

    choice = get_choice(
        "\nDo you:\n1) Open it without much thought\n2) Examine it carefully for hidden mechanisms\n3) Set it aside, wary of unknown magic\n> ", ['1', '2', '3'])

    if choice == '1':
        stats['Conscientiousness']['score'] -= 3
        stats['Openness']['score'] += 5
        stats['Neuroticism']['score'] += 3
        print_slowly(
            "\nAs you break the seal, golden light erupts! The letter disintegrates into butterflies that form a doorway...")
    elif choice == '2':
        stats['Conscientiousness']['score'] += 5
        stats['Openness']['score'] += 2
        print_slowly(
            "\nYou discover tiny runes along the edge. When traced in order, they float upward and rearrange into a map...")
    else:
        stats['Neuroticism']['score'] += 5
        stats['Openness']['score'] -= 1
        print_slowly(
            "\nThe letter begins to glow hotter. Suddenly it unfolds itself, and the handwriting morphs into: 'Too late for caution now...'")

# 🌿 Scene 2: The Sentient Forest


def scene_forest():
    print("\n" + "="*50)
    print("🌿 THE WHISPERING WILLOWS 🌿")
    print("="*50)
    print_slowly(
        "\nYou step into a forest where trees hum in harmony. Their bark shifts to form faces as you pass.")
    print_slowly(
        "A childlike voice calls from the largest oak: 'Lost one! The path branches ahead—choose wisely.'")
    print_slowly("\nBefore you lie three paths:")
    print_slowly(
        "1) Left: Brightly lit with floating lanterns, laughter echoes")
    print_slowly(
        "2) Right: Dark but with bioluminescent plants pulsing rhythmically")
    print_slowly("3) Center: An overgrown trail with faint animal tracks")

    choice = get_choice(
        "\nWhich path calls to you? (1/2/3): ", ['1', '2', '3'])

    if choice == '1':
        stats['Extraversion']['score'] += 6
        stats['Openness']['score'] += 2
        stats['Agreeableness']['score'] += 1
        print_slowly(
            "\nAs you join the revelry, the lanterns brighten. Strangers greet you like an old friend...")

    elif choice == '2':
        stats['Openness']['score'] += 6
        stats['Neuroticism']['score'] += 1
        print_slowly(
            "\nThe plants pulse faster as you walk. Their light reveals hidden murals telling ancient stories...")

    else:  # choice == '3'
        stats['Agreeableness']['score'] += 3
        stats['Conscientiousness']['score'] += 2
        stats['Openness']['score'] += 1
        print_slowly(
            "\nFollowing the tracks leads you to an injured fox. Its golden eyes seem far too knowing...")


# 🏰 Scene 3: The Mirror of Many Selves
def scene_mirror():
    print("\n" + "="*50)
    print("🏰 THE MIRROR OF MANY SELVES 🏰")
    print("="*50)
    print_slowly(
        "\nYou enter a circular chamber where a massive mirror dominates the wall.")
    print_slowly("Instead of your reflection, it shows:")
    print_slowly("- You as a celebrated hero")
    print_slowly("- You as a feared villain")
    print_slowly("- You as an ordinary person living quietly")
    print_slowly(
        "The glass ripples like water as a voice asks: 'Which is the truest version?'")

    choice = get_choice("\nDo you:\n1) Touch the heroic version proudly\n2) Reach for the villainous image curiously\n3) Watch the ordinary life longingly\n4) Turn away from all reflections\n> ", [
                        '1', '2', '3', '4'])

    if choice == '1':
        stats['Extraversion']['score'] += 4
        stats['Agreeableness']['score'] += 3
        print_slowly(
            "\nThe mirror shimmers gold. You feel a surge of confidence as armor materializes on your body...")
    elif choice == '2':
        stats['Openness']['score'] += 3
        stats['Agreeableness']['score'] -= 2
        print_slowly(
            "\nThe glass turns black. Shadows curl around your arms whispering secrets of power...")
    elif choice == '3':
        stats['Agreeableness']['score'] += 2
        stats['Neuroticism']['score'] += 2
        print_slowly(
            "\nThe reflection smiles and extends its hand. For a moment, you feel profound peace...")
    else:
        stats['Neuroticism']['score'] += 3
        stats['Openness']['score'] += 2
        print_slowly(
            "\nThe mirror cracks! The pieces rearrange into a doorway revealing another realm beyond...")


def scene_bridge():
    print("\n" + "="*50)
    print("🌉 THE BRIDGE OF WHISPERS 🌉")
    print("="*50)
    print_slowly(
        "\nYou stand before a chasm spanned by a crumbling bridge. Each step you take makes stones disappear behind you.")
    print_slowly(
        "Ethereal voices whisper warnings and encouragement in equal measure:")
    print_slowly("- 'Turn back! The other side is illusion!'")
    print_slowly("- 'Trust the path—what you fear is just shadows!'")

    choice = get_choice(
        "\nDo you:\n1) Sprint across without hesitation\n2) Test each plank carefully\n3) Sit and listen to the voices first\n> ", ['1', '2', '3'])

    if choice == '1':
        stats['Openness']['score'] += 5
        stats['Neuroticism']['score'] -= 2
        print_slowly(
            "\nThe bridge solidifies beneath your fearless steps! At the midpoint, you find floating gifts left by previous runners...")
    elif choice == '2':
        stats['Conscientiousness']['score'] += 5
        print_slowly(
            "\nAs you probe, invisible hands repair the bridge. A hidden inscription appears: 'Prudence rewards the patient...'")
    else:
        stats['Neuroticism']['score'] += 3
        stats['Openness']['score'] += 3
        print_slowly(
            "\nThe voices coalesce into a spirit who offers cryptic advice before blowing you gently across like a leaf...")


def scene_masquerade():
    print("\n" + "="*50)
    print("🎭 THE MASQUERADE OF TRUTH 🎭")
    print("="*50)
    print_slowly(
        "\nYou're thrust into a ballroom where attendees wear masks that project false emotions:")
    print_slowly("- A laughing mask hides tear-streaked cheeks")
    print_slowly("- A scowling mask covers a serene smile")
    print_slowly(
        "The host announces: 'Remove any mask to see its wearer's truth!'")

    choice = get_choice(
        "\nDo you:\n1) Remove many masks eagerly\n2) Carefully remove one mask\n3) Remove your own mask first\n> ", ['1', '2', '3'])

    if choice == '1':
        stats['Extraversion']['score'] += 7
        stats['Agreeableness']['score'] -= 1
        print_slowly(
            "\nThe crowd gasps as revelations spark both fights and reconciliations. You're given a mask of many faces...")
    elif choice == '2':
        stats['Agreeableness']['score'] += 4
        print_slowly(
            "\nThe person you unmask hugs you, their gratitude making your own mask grow lighter...")
    else:
        stats['Neuroticism']['score'] += 3
        stats['Agreeableness']['score'] += 2
        print_slowly(
            "\nYour bare face glows, causing others to voluntarily remove their masks in your presence...")


def scene_library():
    print("\n" + "="*50)
    print("🏛️ THE LIBRARY OF LIVES 🏛️")
    print("="*50)
    print_slowly(
        "\nBefore you stretches an infinite library where books write themselves in real-time.")
    print_slowly("Some titles call to you:")
    print_slowly("- 'How Your Story Ends (Current Edition)'")
    print_slowly("- 'The Secret Thoughts of Those You Love'")
    print_slowly("- 'Paths Not Yet Taken'")

    choice = get_choice("\nWhich do you read first?\n1) Your ending\n2) Others' thoughts\n3) Alternate paths\n4) None—explore the library itself\n> ", [
                        '1', '2', '3', '4'])

    if choice == '1':
        stats['Neuroticism']['score'] += 5
        print_slowly(
            "\nThe pages shift as you read—your anxiety makes the ending grow darker...")
    elif choice == '2':
        stats['Agreeableness']['score'] += 2
        print_slowly(
            "\nYou learn painful truths, but also hidden kindnesses you'd never suspected...")
    elif choice == '3':
        stats['Openness']['score'] += 5
        print_slowly(
            "\nThe book splits into infinite volumes as you imagine new possibilities...")
    else:
        stats['Openness']['score'] += 5
        print_slowly(
            "\nYou discover the library's blueprints—and a note with your name from a previous explorer...")


def scene_shadow_well():
    print("\n" + "="*50)
    print("👤 THE SHADOW WELL 👤")
    print("="*50)
    print_slowly(
        "\nA bottomless well reflects not your face, but your darkest memory.")
    print_slowly(
        "A rope hangs nearby with a bucket that whispers: 'Draw up what you buried.'")

    choice = get_choice(
        "\nDo you:\n1) Lower the bucket boldly\n2) Drop a pebble instead to test depth\n3) Walk away without looking\n> ", ['1', '2', '3'])

    if choice == '1':
        stats['Openness']['score'] += 5
        print_slowly(
            "\nThe heavy bucket emerges full of black liquid that transforms into glowing butterflies...")
    elif choice == '2':
        stats['Neuroticism']['score'] += 4
        print_slowly(
            "\nThe pebble's echo returns as a melody. The well's darkness lightens slightly...")
    else:
        stats['Conscientiousness']['score'] += 4
        stats['Neuroticism']['score'] += 2
        print_slowly(
            "\nYour shadow detaches and jumps in without you. You feel lighter but incomplete...")


def scene_puzzle_garden():
    print("\n" + "="*50)
    print("🧩 THE PUZZLE GARDEN 🧩")
    print("="*50)
    print_slowly("\nTopiary animals demand you 'prove your worth' to pass:")
    print_slowly(
        "- A lion asks for logic: 'What belongs to you but others use more?'")
    print_slowly("- A fox requests creativity: 'Describe color to the blind!'")
    print_slowly(
        "- A bear offers physical challenge: 'Move this boulder with no tools!'")

    choice = get_choice(
        "\nWhich do you attempt?\n1) Solve the riddle\n2) Give creative answer\n3) Try moving the boulder\n> ", ['1', '2', '3'])

    if choice == '1':
        stats['Conscientiousness']['score'] += 4
        stats['Openness']['score'] += 2
        print_slowly(
            "\nThe lion nods. 'Your mind,' it says, vanishing to reveal a path...")
    elif choice == '2':
        stats['Openness']['score'] += 6
        print_slowly(
            "\nThe fox's leaves bloom into flowers matching your description...")
    else:
        stats['Extraversion']['score'] += 5
        print_slowly(
            "\nThe bear helps after seeing your effort. The boulder crumbles to reveal a key...")


def scene_storm():
    print("\n" + "="*50)
    print("🌪️ THE STORM OF OPINIONS 🌪️️")
    print("="*50)
    print_slowly(
        "\nA tempest of voices swirls around you, each shouting contradictory advice:")
    print_slowly("- 'Trust no one!' / 'Love unconditionally!'")
    print_slowly("- 'Take risks!' / 'Security is everything!'")
    print_slowly("Your cloak billows with each shouted phrase that hits you.")

    choice = get_choice(
        "\nDo you:\n1) Yell your own mantra louder\n2) Weave conflicting advice together\n3) Cover your ears and push through\n> ", ['1', '2', '3'])

    if choice == '1':
        stats['Extraversion']['score'] += 6
        print_slowly(
            "\nThe storm parts before your voice. Those who shared your view fall in step behind you...")
    elif choice == '2':
        stats['Agreeableness']['score'] += 6
        print_slowly(
            "\nThe voices harmonize into a single guiding whisper tailored just for you...")
    else:
        # Slightly reduced for psychological nuance
        stats['Neuroticism']['score'] += 6
        print_slowly(
            "\nThe storm intensifies but you emerge battered yet unchanged...")


def scene_labyrinth():
    print("\n" + "="*50)
    print("🕰️ THE CLOCKWORK LABYRINTH 🕰️")
    print("="*50)
    print_slowly(
        "\nGears grind underfoot as walls rearrange. Two guides offer help:")
    print_slowly("- A hurried rabbit with 12 ticking pocket watches")
    print_slowly("- A sloth moving in slow motion who blinks once per minute")

    choice = get_choice(
        "\nWho do you follow?\n1) The rabbit\n2) The sloth\n3) Neither—mark your own path\n> ", ['1', '2', '3'])

    if choice == '1':
        stats['Conscientiousness']['score'] += 4
        print_slowly(
            "\nYou reach the center quickly but find your hair has grayed from time acceleration...")
    elif choice == '2':
        stats['Conscientiousness']['score'] += 3
        print_slowly(
            "\nThe path becomes clear as you observe each slow mechanical shift...")
    else:
        stats['Openness']['score'] += 3
        stats['Extraversion']['score'] += 6
        print_slowly(
            "\nYour unique route causes new corridors to form, surprising both guides...")


def scene_cocoon():
    print("\n" + "="*50)
    print("🦋 THE COCOON CHAMBER 🦋")
    print("="*50)
    print_slowly(
        "\nA luminous cocoon hangs before you, pulsing in sync with your heartbeat.")
    print_slowly(
        "A sign reads: 'Enter to become your next self. Warning: Irreversible.'")

    choice = get_choice(
        "\nDo you:\n1) Climb in immediately\n2) Ask what changes it will make\n3) Take a thread but refuse entry\n> ", ['1', '2', '3'])

    if choice == '1':
        stats['Openness']['score'] += 7
        print_slowly(
            "\nThe cocoon dissolves to reveal you with new abilities—but forgotten memories...")
    elif choice == '2':
        stats['Conscientiousness']['score'] += 5
        print_slowly(
            "\nThe cocoon shows your potential forms. The choice grows harder...")
    else:
        stats['Agreeableness']['score'] += 3
        stats['Conscientiousness']['score'] += 3
        print_slowly(
            "\nThe thread weaves into your clothes, giving partial transformation powers...")


def scene_throne():
    print("\n" + "="*50)
    print("👑 THE EMPTY THRONE 👑")
    print("="*50)
    print_slowly(
        "\nA magnificent throne sits atop a dais. Its crown hovers midair, waiting.")
    print_slowly(
        "The last inscription reads: 'Rule wisely—your laws shape reality here.'")

    choice = get_choice(
        "\nDo you:\n1) Sit and declare first edict\n2) Place crown on another\n3) Smash the throne\n> ", ['1', '2', '3'])

    if choice == '1':
        stats['Extraversion']['score'] += 7
        print_slowly(
            "\nThe throne binds to you. Subjects appear, expecting guidance...")
    elif choice == '2':
        stats['Conscientiousness']['score'] -= 5
        stats['Agreeableness']['score'] += 6
        print_slowly(
            "\nThe chosen person gains power—and undying loyalty to you...")
    else:
        stats['Neuroticism']['score'] += 6
        print_slowly(
            "\nThe rubble forms a democracy monument. New voices rise...")


def scene_doorway():
    print("\n" + "="*50)
    print("🌌 THE DOORWAY OF ECHOES 🌌")
    print("="*50)
    print_slowly(
        "\nAn archway shows your greatest regret playing on loop. A spectral hand offers:")
    print_slowly("- A button to undo that moment")
    print_slowly("- A pill to forget it")
    print_slowly("- A lens to reframe its meaning")

    choice = get_choice(
        "\nWhich do you take?\n1) Undo button\n2) Forget pill\n3) Reframing lens\n> ", ['1', '2', '3'])

    if choice == '1':
        stats['Neuroticism']['score'] += 5
        print_slowly(
            "\nThe timeline rewinds... but new unintended consequences unfold...")
    elif choice == '2':
        stats['Neuroticism']['score'] += 4
        print_slowly(
            "\nThe memory fades, but you sense a hollow space where it was...")
    else:
        stats['Openness']['score'] += 4
        print_slowly(
            "\nThe scene transforms—you see how the pain strengthened unseen parts of you...")


# 🎭 Run All Scenes
scene_letter()
scene_forest()
scene_mirror()
scene_bridge()
scene_masquerade()
scene_library()
scene_shadow_well()
scene_puzzle_garden()
scene_storm()
scene_labyrinth()
scene_cocoon()
scene_throne()
scene_doorway()

print_slowly("\n✨ The game ends not with triumph—but with transformation.")
print_slowly("🧭 As the world reshapes itself around you, you realize: the magic wasn't the realm—it was what it revealed within you.")

for trait in stats:
    stats[trait]['score'] = max(
        0, min(100, stats[trait]['score']))

total = sum(stats[trait]['score'] for trait in stats)
for trait in stats:
    stats[trait]['percentage'] = round(
        (stats[trait]['score'] / total) * 100, 1)

print("\n" + "🧙‍♂️" * 20)
print("YOUR PSYCHOLOGICAL PROFILE")
print("🧙‍♂️" * 20)

for trait in stats:
    print(f"\n🔮 {trait}: {stats[trait]['percentage']}%")
    print(f"   Sub-traits: {', '.join(stats[trait]['subtraits'])}")

labels = [trait for trait in stats]
sizes = [stats[trait]['percentage'] for trait in stats]
explode = [0.1 if max(sizes) == size else 0 for size in sizes]

fig, ax = plt.subplots(figsize=(10, 6))
ax.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
       shadow=True, startangle=90, colors=plt.cm.Pastel1.colors)
ax.axis('equal')
plt.title(f"{name}'s Mindscape Composition", fontsize=16, pad=20)
plt.tight_layout()

max_trait = max(stats, key=lambda x: stats[x]['percentage'])
archetypes = {
    'Openness': ("🌌 The Dreamweaver", "You see possibilities where others see boundaries. Your imagination constructs new realities."),
    'Conscientiousness': ("🧭 The Architect", "You build order from chaos. Every action is a deliberate brick in your life's structure."),
    'Extraversion': ("🔥 The Sunheart", "You radiate energy that animates the world around you. Social connections fuel your magic."),
    'Agreeableness': ("🌿 The Harmonist", "You weave understanding between beings. Your empathy creates invisible bridges."),
    'Neuroticism': ("🌙 The Stormseer", "You feel deeply—both shadows and light. Your emotional intensity is its own power.")
}

print(f"\n✨ YOUR ARCHETYPE: {archetypes[max_trait][0]}")
print(f"📜 {archetypes[max_trait][1]}")
final_df = pd.DataFrame({
    "Trait": list(stats.keys()),
    "Score": [stats[t]['score'] for t in stats],
    "Percentage": [stats[t]['percentage'] for t in stats],
    "Sub-traits": [", ".join(stats[t]['subtraits']) for t in stats]
})
print("\n🧠 Final Trait Table:\n")
print(final_df.to_string(index=False))

if input("\nPreserve your journey in the Hall of Reflections? (yes/no): ").lower() == 'yes':
    profile = {
        'Name': [name],
        'Archetype': [archetypes[max_trait][0]],
        **{trait: [stats[trait]['percentage']] for trait in stats}
    }
    df = pd.DataFrame(profile)

    if os.path.exists('auralith_profiles.csv'):
        existing = pd.read_csv('auralith_profiles.csv')
        updated = pd.concat([existing, df], ignore_index=True)
        updated.to_csv('auralith_profiles.csv',
                       index=False, encoding='utf-8-sig')
    else:
        df.to_csv('auralith_profiles.csv', index=False, encoding='utf-8-sig')

    print_slowly(
        "\n📜 Your essence has been preserved in the eternal archives.")
    print_slowly(
        "Should you return to Auralith, your profile will remember you.")


print_slowly(
    "\n🎭 Until we meet again, traveler. Remember—every choice reveals, every revelation transforms.")
plt.show()
