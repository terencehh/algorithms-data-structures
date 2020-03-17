# Given a text and Pattern
# create a Z array str[0..n]
# where str[i] represent the longest
# substring possible which is a prefix of text

# After z-array done
# Find the index values in z-array with length == len(pattern)

# subtract the index value by len(pattern) + 1 to
# get the index value in the original text which matches the pattern


def z_algorithm(text, pattern):

    debug_str = "abcabcabdabc"
    debug_str = "aaaaaa"
    debug_str = "a" #<<< there's an index out of range error. cuz of line 40. :z_arr[1] = counter, not sure if they will give a string with length one, but actl step1 is not needed. i think. commented it out to test
    debug_str = "abcde"
    debug_str = "aabcaabxaaz"
    # Define Z-array
    z_arr = [0] * len(debug_str)

    # z_arr = [0] * len(text + pattern)
    # Define Z-box
    z_box = [None] * len(debug_str)
    # Define R
    r = 0
    # Define L
    l = 0

    # perform checking if string is of length 1

    # Compute Zk values

    for k in range(1, len(debug_str)):

        if k > r:

            print("Explicitly computing from ", k)

            # Explicitly match str[i..q] with str[0..q-i] until
            # mismatch is found at some q + 1 >= i
            counter = 0
            for i in range(k, len(debug_str)):
                if debug_str[i] == debug_str[counter]:
                    counter += 1
                else:
                    break

            z_arr[k] = counter

            if z_arr[k] > 0:
                z_box[k] = (k, k + counter - 1)
                r = k + counter - 1
                l = k

            else:
                z_box[k] = z_box[k-1]
                # r and l do not change

        elif k <= r:

            # r and l do not change

            prev_z = z_arr[k-l]
            beta_length = r - k + 1  # the length includes the alphabet starting from k to r inclusive

            if prev_z < beta_length:
                z_arr[k] = prev_z

            elif prev_z > beta_length:
                z_arr[k] = beta_length
            else:
                counter = 0
                start = r - l + 1
                for i in range(r+1, len(debug_str)):
                    if debug_str[i] == debug_str[start]:
                        counter += 1
                        start += 1
                    else:
                        break

                z_arr[k] = counter + r - k + 1

            z_box[k] = (l, r)

    print(z_arr)
    print(z_box)


def main():
    # n = str(input("Please enter a text: "))
    # pattern = str(input("Please enter a pattern: "))
    z_algorithm("1", "123")


if __name__ == "__main__":
    main()



