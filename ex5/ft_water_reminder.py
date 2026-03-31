# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_water_reminder.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tsiarran <tsiarran@student.42antananari    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/03/30 23:12:47 by tsiarran          #+#    #+#              #
#    Updated: 2026/03/31 08:46:54 by tsiarran         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def	ft_water_reminder():
	days = int(input("Days since last watering: "))
	if days > 2:
		print("Water the plants!")
	else :
		print("Plants are fine")
