# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_recursive.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tsiarran <tsiarran@student.42antananari    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/03/31 07:02:34 by tsiarran          #+#    #+#              #
#    Updated: 2026/03/31 09:20:16 by tsiarran         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def	call_me(days, day):
	print(f"Day ", day)
	if day in range(days - 1):
		call_me(days, day + 1)

def	ft_count_harvest_recursive():
	days = int(input("Days until harvest: "))
	day = 1
	call_me(days, day)
	print("Harvest time!")
	
