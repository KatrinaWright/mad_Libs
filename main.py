# Creating a mad lib program
# by: Katrina Wright
# started May 25th, 2023

# Create containers for holding user inputs
alan = "a/an"
adjective1 = "one"
part_body = "two"
noun1 = "three"
plural_noun = "four"
male_name = "five"
noun_place = "six"
adverb = "seven"
adjective2 = "eight"
adjective3 = "nine"
adjective4 = "ten"
noun2 = "eleven"
noun3 = "twelve"
noun4 = "thirteen"
noun5 = "fourteen"
adjective5 = "fifteen"
adjective6 = "sixteen"
adjective7 = "seventeen"
adjective8 = "eighteen"
plural_noun2 = "nineteen"
number1 = "twenty"
number2 = "twenty-one"
number3 = "twenty-two"
part_body2 = "twenty-three"
verb_ing = "twentry-four"
adverb2 = "twenty-five"
verb = "twenty-six"
verb2 = "twenty-seven"
occupation = "twenty-eight"
plural_noun3 = "twenty-nine"
plural_noun4 = "thirty"
plural_noun5 = "thirty-one"


# list storys with input spots
cinderella_story = f"""
There once was {alan} {adjective1} young girl named Cinderella who lived with her {adjective2} stepmother and two {adjective3} stepsisters.
She waited on them hand and {part_body}, but they treated her like {alan} {noun1}.
Cinderella heard about a ball the prince was throwing, but she didn't have {alan} {adjective4} gown to wear.
Then, out of the clear, blue {noun2}, her fairy {noun3}-mother appeared and waved her magic {noun4}.
Cinderella's ragged clothes turned into a beautiful {noun5}, and her worn work shoes became a pair of glass {plural_noun}.
Cinderella went to the ball and danced with Prince {male_name}, who fell madly in love with her.
But at the stroke of midnight she had to flee, losing one of her glass {plural_noun}.
The prince travelled throughout the kingdom, trying to find the matching {plural_noun}.
He visited the {noun_place} of every young girl until he found Cinderella, who had the other half of the {plural_noun}.
Prince {male_name} and Cinderella soon were married and lived {adverb} ever after!  
"""

witches_stew = f"""
Need to make {alan} {adjective1} princess fall into a deep {adjective2} sleep? 
Here is a recipe that will bring incredibly {adjective3} results.
First, put a large {adjective4} cauldron, filled to the brim with {plural_noun}, on an open {noun1} and heat to {number1} degrees. 
When it begins to boil, add {alan} {part_body} from a newt and {number2} freshly caught {adjective5} {plural_noun2}. 
Mash them up well and mix with the {part_body2} of a toad and the {noun2} of a small, furry {noun3}.
Once again, bring to {alan} {adjective6} boil and cook for {number3} minutes. 
Now you can offer the brew to any unsuspecting {adjective1} princess - they fall for it every time.
But beware: No matter how strong the {adjective2} potion is, true love will reverse its spell every time!
"""

princess_how_to = f"""
It is difficult not to envy a young woman who has everything her {part_body} desires.
But history shows it isn't easy being a princess.
You have to maintain {adjective1} standards and abide by {adjective2} rules. For example:
* A princess should always be kind to, and understanding of, her royal {plural_noun}.
* A princess knows that {alan} {adjective2} smile is preferable to {alan} {adjective3} frown.
* A princess should be a patron of the arts, well-versed in classical {noun1}, and {adverb} familar with {adjective4} authors and their {adjective5} works. 
* A princess should never make {alan} {adjective6} decision. She should always think before {verb_ing}.
* And when she does speak, she should be articulate and, if possible, very {adjective7}.
* And, of course, a princess must be prepared to marry {alan} {adjective8} prince and live {adverb2} ever after.
"""

mermaid_life = f"""
Life under the sea is full of wonder and {plural_noun} --- especially when you're a mermaid and {alan} {adjective1} underwater princess like me!
I live on the ocean floor in {alan} {adjective2} castle made of coral {plural_noun2}.
My dad is King {male_name}, ruler of the entire {noun1}.
My friends are fish, dolphins, and an underwater {noun2}. 
We spend our days exploring {noun3} reefs and searching for sunken {plural_noun3}.
Sometimes I wonder what it would be like to {verb} on land. 
I've heard that people there have {part_body} instead of fins!
And that thy {verb2} around from place to place in motorized {plural_noun4} and wear {adjective3} {plural_noun5} on their {part_body2}.
Someday I hope to visit this place so I can meet a handsome {occupation} and fall {adverb} in love. 
That would be a mermaid's {noun4} come true!
"""
# user inputs strings into containers
## starting with welcome message
welcome_message = f"""
Welcome to the Mad Libs program! Let's create a silly story together!
"""
print(welcome_message)

## making functions for each story
def input_mermaid_life():
    print("let's make a story about mermaids!")
    adjective1, adjective2, adjective3 = input("Please provide three adjectives: ").split() 
    return adjective1, adjective2

###Variables needed for mermaid_life
### [plural_noun, plural_noun2, plural_noun3, plural_noun4, plural_noun5, noun1, noun2, noun3, noun4, adjective1, adjective2, adjective3, male_name, occupation, verb, verb2, part_body, part_body2, adverb]


# input_mermaid_life()
# Quality check user input 




# Create function that inserts containers into story



# function for deciding a versus an



# randomize the story that is given when opening the app


# debugging and tests
#print(cinderella_story)

#print(witches_stew)

#print(princess_how_to)

print(mermaid_life)
# ask user if they would like to do another story



