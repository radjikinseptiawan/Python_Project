
class encryption:
    def vigenere(self,text,key = 'radjikinseptiawan',direction=1):
        key_index = 0
        alphanumeric = 'abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        final_message = ''

        for char in text.lower():
            key_char = key[key_index % len(key)]
            key_index += 1

            offset = alphanumeric.index(key_char)
            index = alphanumeric.find(char)
            new_index = (index + offset*direction)

            final_message += alphanumeric[new_index]

        return final_message