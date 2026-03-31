# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_age.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tsiarran <tsiarran@student.42antananari    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/03/30 23:04:39 by tsiarran          #+#    #+#              #
#    Updated: 2026/03/31 08:46:49 by tsiarran         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def	ft_plant_age():
	days = int(input("Enter plant age in days: "))
	if days > 60:
		print("Plant is ready to harvest!")
	else:
		print("Plant needs more time to grow.")
