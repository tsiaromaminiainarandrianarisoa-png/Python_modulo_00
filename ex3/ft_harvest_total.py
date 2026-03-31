# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_harvest_total.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tsiarran <tsiarran@student.42antananari    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/03/30 22:57:26 by tsiarran          #+#    #+#              #
#    Updated: 2026/03/31 08:46:45 by tsiarran         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def	ft_harvest_total():
	first = int(input("Day 1 harvest: "))
	second = int(input("Day 2 harvest: "))
	third = int(input("Day 3 harvest: "))
	print("Total1 harvest: ", first + second + third)
