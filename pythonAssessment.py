
article_text = """
ACME Inc. Unveils Revolutionary Apple Pie Machine, Transforming Baking with Automation

ACME Inc., a leading innovator in culinary technology, has launched a groundbreaking new device that promises to revolutionize the way apple pies are made. Dubbed the “Apple Pie Master,” this machine combines cutting-edge technology with traditional baking techniques to automate the entire pie-making process, ensuring perfect pies every time.

At a press conference held at ACME Inc.'s headquarters in Springfield, the company's CEO, Jane Doe, introduced the Apple Pie Master to an eager audience of journalists, culinary experts, and industry insiders. "Our goal has always been to make cooking and baking accessible and enjoyable for everyone, and with the Apple Pie Master, we are making a giant leap forward," Doe stated.

The Apple Pie Master is designed to simplify the baking process while maintaining the quality and taste of a homemade pie. The machine is equipped with AI-driven sensors that can analyze the quality of ingredients, adjust cooking times, and even replicate intricate baking techniques perfected by master chefs. “This isn't just about saving time; it's about enhancing the baking experience and ensuring consistent results,” Doe explained.
Unpacking the Technology

The heart of the Apple Pie Master lies in its advanced artificial intelligence system. This system is programmed to perform tasks such as peeling and slicing apples, mixing ingredients, and rolling out pie crusts. According to ACME Inc.'s head of product development, Dr. Emily Clark, “The AI not only replicates human actions but learns from each pie made, adjusting its techniques to improve the next one.”

Another innovative feature of the Apple Pie Master is its real-time monitoring capabilities. Cameras and sensors inside the machine provide continuous feedback during the pie-making process, allowing the AI to make micro-adjustments to the temperature and cooking times as needed. This ensures that each pie is baked to golden perfection.

User-Friendly Features

ACME Inc. has designed the Apple Pie Master with user experience in mind. The machine features a sleek, user-friendly interface with pre-programmed settings for different pie recipes. 
Users can select options for crust type, spice levels, and even the variety of apples they want to use. “We want to cater to all taste preferences, from the traditional to the adventurous,” said marketing director, Tom Nguyen.

The machine also includes a mobile app, allowing users to start the baking process from their smartphones. This app not only controls the machine but also provides users with tips, recipes, and the option to order ingredients directly through ACME Inc.'s partners.

Environmental and Economic Impact

ACME Inc. is also proud of the Apple Pie Master’s environmental credentials. The machine is built from recycled materials and designed to operate with minimal energy consumption. “Sustainability is at the core of all our product designs,” emphasized environmental consultant Lisa Green, who collaborated on the project.

Economically, the Apple Pie Master could have significant implications for both commercial and home bakers. By reducing the time and skill required to make high-quality pies, it opens up new business opportunities for small bakeries and restaurants, and it provides a cost-effective solution for busy consumers who crave homemade desserts without the fuss.

Market Response and Availability

The response to the Apple Pie Master has been overwhelmingly positive. Early adopters and reviewers have praised its ease of use and the quality of the pies it produces. Culinary blogger Mark Spencer commented, “It’s like having a professional baker in your kitchen. The pies are consistently excellent, with perfectly flaky crusts and rich, flavorful fillings.”

ACME Inc. plans to make the Apple Pie Master available online and in select retail stores starting next month. The company has set a competitive price point to make this innovative technology accessible to a broad audience.

The Future of Automated Baking

Looking ahead, ACME Inc. plans to expand its range of automated baking machines. “The Apple Pie Master is just the beginning,” said CEO Jane Doe. “We’re exploring machines for other types of desserts and complex dishes. Our vision is to automate parts of the cooking process without sacrificing the art of cooking.”
The Apple Pie Master from ACME Inc. represents a significant advancement in the field of culinary technology. By automating the process of baking apple pies, this machine not only makes baking more accessible but also sets a new standard for the integration of technology in traditional cooking practices. As more consumers and businesses adopt this technology, it could well redefine our cooking experiences and expectations.
"""


# Get individual words while ignoring punctuation and special characters.
def get_words(text):

    words = []
    current_word = ""

    for character in text:

        if character.isalnum():
            current_word += character.lower()

        else:
            if current_word != "":
                words.append(current_word)
                current_word = ""

    # Make sure the final word is not lost.
    if current_word != "":
        words.append(current_word)

    return words


# 1. COUNT A SPECIFIC WORD

def count_specific_word(text, search_word):

    words = get_words(text)
    count = 0

    search_word = search_word.lower()

    for word in words:

        if word == search_word:
            count += 1

    return count


# 2. IDENTIFY MOST COMMON WORD

def identify_most_common_word(text):

    # The assignment requires None for an empty string.
    if text.strip() == "":
        return None

    words = get_words(text)

    if len(words) == 0:
        return None

    word_counts = {}

    for word in words:

        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    most_common_word = None
    highest_count = 0

    for word in word_counts:

        if word_counts[word] > highest_count:
            highest_count = word_counts[word]
            most_common_word = word

    return most_common_word


# 3. CALCULATE AVERAGE WORD LENGTH

def calculate_average_word_length(text):

    # The assignment requires 0 for an empty string.
    if text.strip() == "":
        return 0

    words = get_words(text)

    if len(words) == 0:
        return 0

    total_length = 0

    for word in words:
        total_length += len(word)

    return total_length / len(words)


# 4. COUNT PARAGRAPHS

def count_paragraphs(text):

    # The assignment specifically requires 1 for an empty string.
    if text.strip() == "":
        return 1

    paragraph_count = 0
    inside_paragraph = False

    lines = text.split("\n")

    for line in lines:

        if line.strip() != "":

            if inside_paragraph == False:
                paragraph_count += 1
                inside_paragraph = True

        else:
            inside_paragraph = False

    return paragraph_count


# 5. COUNT SENTENCES

def count_sentences(text):

    # The assignment specifically requires 1 for an empty string.
    if text.strip() == "":
        return 1

    sentence_count = 0
    index = 0

    while index < len(text):

        character = text[index]

        if (
            character == "."
            or character == "!"
            or character == "?"
        ):

            sentence_count += 1

            # Treat consecutive sentence punctuation as one ending.
            while index + 1 < len(text):

                next_character = text[index + 1]

                if (
                    next_character == "."
                    or next_character == "!"
                    or next_character == "?"
                ):
                    index += 1
                else:
                    break

        index += 1

    return sentence_count


# RUN THE PROGRAM

specific_word = "the"

specific_word_count = count_specific_word(
    article_text,
    specific_word
)

most_common = identify_most_common_word(
    article_text
)

average_length = calculate_average_word_length(
    article_text
)

paragraphs = count_paragraphs(
    article_text
)

sentences = count_sentences(
    article_text
)


# DISPLAY RESULTS

print(
    "Number of times",
    specific_word,
    "appears:",
    specific_word_count
)

print(
    "Most common word:",
    most_common
)

print(
    "Average word length:",
    average_length
)

print(
    "Number of paragraphs:",
    paragraphs
)

print(
    "sentence: analysis",
    sentences
)


