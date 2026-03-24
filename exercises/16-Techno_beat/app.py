def lyrics_generator(list_data): 
    text = ""
    for i in range(len(list_data)):
        if list_data[i] == 0:
            text += "Boom "
        elif list_data[i] == 1:
            text += "Drop the bass "
        if i >= 2:
            if list_data[i-2] == 1 and list_data[i-1] == 1 and list_data[i] == 1:
                text += "!!!Break the bass!!! "            
    return text


# Your code above, nothing to change after this line
print(lyrics_generator([0,0,1,1,0,0,0]))
print(lyrics_generator([0,0,1,1,1,0,0,0]))
print(lyrics_generator([0,0,0]))
print(lyrics_generator([1,0,1]))
print(lyrics_generator([1,1,1]))
