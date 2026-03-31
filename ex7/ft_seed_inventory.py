# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_seed_inventory.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tsiarran <tsiarran@student.42antananari    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/03/31 08:36:29 by tsiarran          #+#    #+#              #
#    Updated: 2026/03/31 10:14:24 by tsiarran         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def	ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
	seed = seed_type.capitalize()
	units = ("packets","grams","area")
	back = (" available", " total", " square meters")
	loc = 0
	front = ""
	res = ""
	while loc < 3:
		if unit == units[loc]:
			res = back[loc]
			if loc == 2:
				front = "covers "
			break
		loc = loc + 1
	if res == "":
		return (print("Unknown unit type"))
	print(seed + " seeds: " + front + str(quantity)+ " " + unit + res)
