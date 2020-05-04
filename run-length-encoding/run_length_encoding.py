def decode(string):
    decoded_string = ''
    for i in range(len(string)):
        prev = string[i - 1]
        curr = string[i]

        if curr.isalpha() or curr == ' ':
            decoded_string += curr

        elif curr.isnumeric():
            next = string[i + 1]
            if next.isnumeric():
                continue
            elif prev.isnumeric():
                decoded_string += next * (int(prev + curr) - 1)
            else:
                decoded_string += next * (int(curr) - 1)
    return decoded_string


def encode(string):
    encoded_string = ''

    count = 1
    for i in range(len(string)):
        first = 0
        prev = string[i - 1]
        curr = string[i]
        last = len(string) - 1

        if i == first:
            continue
        elif curr == prev:
            count += 1
            if i == last:
                encoded_string += str(count)
                encoded_string += curr
        else:
            if count > 1:
                encoded_string += str(count)
                encoded_string += prev
                if i == last:
                    encoded_string += curr
            else:
                encoded_string += prev
                if i == last:
                    encoded_string += curr
            count = 1
    return encoded_string
