# def calculate_love_score(user_name, partner):
#     # ttl_count = int(0)
#     percentage_count_for_true = int(0)
#     for tl_ltr in "TRUE":
#
#         count = int(0)
#         for usr_nm_ltr in user_name + partner:
#             if tl_ltr == usr_nm_ltr:
#                 count += 1
#
#         percentage_count_for_true = percentage_count_for_true + count
#
#         print(f"{tl_ltr} occurs {count} times")
#     print(f"Total = {percentage_count_for_true}")
#
#     percentage_count_for_love = int(0)
#     for tl_ltr in "LOVE":
#
#         count = int(0)
#         for usr_nm_ltr in user_name + partner:
#             if tl_ltr == usr_nm_ltr:
#                 count += 1
#
#         percentage_count_for_love = percentage_count_for_love + count
#
#         print(f"{tl_ltr} occurs {count} times")
#     print(f"Total = {percentage_count_for_love}")
#     print(f"Love Score = ", str(percentage_count_for_true) + str(percentage_count_for_love))
#
#
# calculate_love_score(user_name="KANYE WEST", partner="KIM KARDASHIAN")


def calculate_love_score(user_name, partner):
    def count_letters(word, names):
        return sum(names.count(letter) for letter in word)

    combined_names = user_name + partner
    true_count = count_letters("TRUE", combined_names)
    love_count = count_letters("LOVE", combined_names)

    print(f"Total for TRUE = {true_count}")
    print(f"Total for LOVE = {love_count}")
    print(f"Love Score = {true_count}{love_count}")


calculate_love_score("KANYE WEST", "KIM KARDASHIAN")