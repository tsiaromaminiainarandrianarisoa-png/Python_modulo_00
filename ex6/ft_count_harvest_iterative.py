# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_iterative.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tsiarran <tsiarran@student.42antananari    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/03/30 23:51:23 by tsiarran          #+#    #+#              #
#    Updated: 2026/03/31 08:46:58 by tsiarran         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def	ft_count_harvest_iterative():
	days = int(input("Days until harvest: "))
	n = 1
	while n in range(days):
		print("Day ", n)
		n = n + 1
	print("Harvest time!")
