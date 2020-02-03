##############################################################################
#                                                                            #
#             bf2_oldschool.py - Weapon Punisher by MisiekBest               #
#	                    --- http://vis-clan.pl ---                       #
#                     --- http://bfo.misiekbest.pl ---                       #
#                                                                            #
#    Released: 28.12.2009                                                    #
#    Script Version: 0.9c                                                    #
#	 Copyright (C) 2009-2010  Michal 'MisiekBest' Pawlikowski                 #
#                                                                            #
#    This program is free software: you can redistribute it and/or modify    #
#    it under the terms of the GNU General Public License as published by    #
#    the Free Software Foundation, either version 3 of the License, or       #
#    any later version.                                                      #
#                                                                            #
#    This program is distributed in the hope that it will be useful,         #
#    but WITHOUT ANY WARRANTY; without even the implied warranty of          #
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the           #
#    GNU General Public License for more details.                            # 
#                                                                            #
#    You should have received a copy of the GNU General Public License       #
#    along with this program.  If not, see http://www.gnu.org/licenses/ .    #
#                                                                            #
##############################################################################
"""
################
# What it is?: #
#########################################################
# BF2 Oldschool is a Battlefield 2                      #
# python script made for few things:                    #
# - Restrict some weapons on server                     #
# - Kick or kill player for using restricted weapon     #
# - Kick commander (or just throw info)                 #
# - Manage script via rcon                              #
#########################################################


###################
# How to install: #
##################################################################
# 1. Go to mods/bf2/python/game/ direcory located on your server #
# (ex. BF2_v1.1.2965/mods/bf2/python/game/)                      #
# 2. Paste there this file                                       #
# 3. Edit __init__.py file and add this two lines:               #
# import bf2_oldschool                                           #
# bf2_oldschool.init()                                           #
# 4. Restart/run your server :)                                  #
##################################################################


###################################
# How to manage sctipt via rcon?: #
###############################################################################################
# This script has 'diffrent' manage method. Why diffrent?                                     #
# Usually admins can manage their scripts using in game chat.                                 #
# Yes, its easiest way, but not efficient. So i decided to use                                #
# little hook with rcon <variable>. It will always generate info                              #
# about error (in game console) but it will work!                                             #
#                                                                                             #
# First you must remember to put your/admin's nickname in settings.                           #
# Rcon will work only for players that are in ADMIN_LIST.                                     #
# See ADMIN SETTINGS section for more info.                                                   #
#                                                                                             #
# TO RUN COMMAND:                                                                             #
#                                                                                             #
# 1. Open your in-game console (by pressing ~ on your keyboard)                               #
# 2. Every command you must execute using phrase: rcon bfo <command> <optional_value>         #
#                                                                                             #
# You can access to this help in game by using 'rcon bfo help' command.                       #
# You can return all main settings by using 'rcon bfo status' command.                        #
#                                                                                             #
# Here is list of all commands:                                                               #
# ############## OLDSCHOOL LEVEL ##############                                               #
# #############################################                                               #
# olevel         # Return number of oldschool level                                           #
# olevel [value] # Set oldschool level to given value                                         #
#                                                                                             #
# ############## PUNISH METHOD  ##############                                                #
# ############################################                                                #
# punish         # Return number of punish method                                             #
# punish [value] # Set punish method to given value                                           #
#                                                                                             #
# ##############   MISC WEAPONS   ##############                                              #
# ##############################################                                              #
# c4         # Return status of C4 restriction                                                #
# c4 [value] # Enable or disble C4 restriction. 0-Disable  1-Enable                           #
# claymore         # Return status of CLAYMORE restriction                                    #
# claymore [value] # Enable or disble CLAYMORE restriction. 0-Disable  1-Enable               #
# mgs         # Return status of MOUNTED MGS restriction                                      #
# mgs [value] # Enable or disble MOUNTED MGS restriction. 0-Disable  1-Enable                 #
# tow         # Return status of TOW MISSILE restriction                                      #
# tow [value] # Enable or disble TOW MISSILE restriction. 0-Disable  1-Enable                 #
#                                                                                             #
# ##############   KICKER SYSTEM (punish 2)   ##############                                  #
# ##########################################################                                  #
# kick_frags         # Return number of how many kills from restricted weapon to kick player  #
# kick_frags [value] # Set HOW_MANY_KILLS_TO_KICK to given value                              #
# kick_time          # Return minutes for how long player should be kicked out.               #
# kick_time [value]  # Set minutes for how long player should be kicked out.                  #
#                                                                                             #
# ##############    ANTI COMMANDER    ##############                                          #
# ##################################################                                          #
# anticomm           # Return status of ANTICOMMANDER system                                  #
# anticomm [value]   # Enable or disble commander restriction. 0-Disable  1-Enable            #
# commkick           # Return status of COMMANDER KICKER system                               #
# commkick [value]   # Enable or disble commander kicking. 0-Disable  1-Enable                #
# commkick_time          # Return minutes for how long commander should be kicked out.        #
# commkick_time [value]  # Set minutes for how long commander should be kicked out.           #
#                                                                                             # 
#                                                                                             #
###############################################################################################

CHANGELOG:

0.9c:
- Added "NO SNIPERS" restriction mode (OLDSCHOOL_LEVEL = 6)
"""





################################################################################
################################################################################
##->                        GLOBAL CONFIGURATION                            <-##
################################################################################
################################################################################

###################
# OLDSCHOOL LEVEL #
#################################################################################################
# Here you can decide which group of weapons should be restricted                               # 
# Set OLDSCHOOL_LEVEL to one of these values:                                                   #
# 0 - Completly disable script!                                                                 #
# 1 - MEDICS ONLY (with med unlocks!)                                                           #
# 2 - MEDICS ONLY (without med unlocks!)                                                        #
# 3 - KNIFE, PISTOL, SHOCKPADDLE (only these weapons are allowed! Other will be punished.       #
#     (NOTE: OLDSCHOOL LEVEL 3 WILL WORK ONLY WITH PUNISH METHOD 2 (kicking)!!!)                #
# 4 - NO UNLOCKS (all kits but without unlocks)                                                 #
# 5 - NO OLDSCHOOL LEVEL, JUST USE OTHER SETTINGS (in.ex.: anticommander or c4, claymore etc.)  #
# 6 - NO SNIPERS                                                                                @
#################################################################################################
OLDSCHOOL_LEVEL = 6



###################
#   MISC WEAPONS  #
#####################################################################
# Here you can enable or disable punishing for using                #
# miscellaneous wapons: c4, claymore, stationary mgs and tow missle #
# Set each variable to 0 or 1                                       #
# 0 - DISABLE                                                       #
# 1 - ENABLE                                                        #
#####################################################################
NO_C4 = 0
NO_CLAYMORE = 1
NO_MOUNTED_MGS = 0 #NOTE: WORKS ONLY WITH PUNISH METHOD 2
NO_TOW_MISSILE = 0 #NOTE: WORKS ONLY WITH PUNISH METHOD 2



####################
#   PUNISH METHOD  #
####################################################################################################################
# Here you can choose how player should be punished for using restricted weapon.                                   #
# Set PUNISH_METHOD to one of these values:                                                                        #
# 0 - NO PUNISH, ONLY WARNING. Warning can be set in WARNING_LVL0 (put %s for player name)                         #
#     NOTE: this will produce massive spam if player                                                               # 
#     will start switching weapons for example from allowed pistol to forbidden                                    #
#     g36e, then pistol and then again g36e etc.                                                                   #
#                                                                                                                  #
# 1 - KILL PLAYER JUST AFTER RESPAWN WITH FORBIDDEN WEAPON.                                                        #
#     Killing msg can be set in WARNING_LVL1 (put %s for player name)                                              #
#     NOTE: if c4 or clay is forbidden player will be punished after                                               #
#     switching to them by pressing 5 or 6 key                                                                     #
#                                                                                                                  #
# 2 - KICK PLAYER AFTER HOW_MANY_KILLS_TO_KICK TIMES                                                               #
#     (PUNKBUSTER PROTECTION MUST BE ENABLED!)                                                                     #
#     Here you can also set few things:                                                                            #
#     HOW_MANY_KILLS_TO_KICK - After how many frags player should be kicked out?                                   #
#                                                                                                                  #
#     WARNING_AFTER_FRAG - This message will appear when player kill somebody with forbidden weapon                #
#                          (put %s for player name)                                                                #
#                                                                                                                  #
#     RESTRICTED_WEAPON_KICK_MSG - This msg appears in game when script is kicking player (put %s for player name) #
#                                                                                                                  #
#     RESTRICTED_WEAPON_KICK_REASON - This msg gets player after kick - in cool punkbuster window :)               #
#                                                                                                                  #
#     RESTRICTED_WEAPON_KICK_IN_MINUTES - Here you can decide for how long player should be kicked. Use wisely ;)  #
####################################################################################################################
PUNISH_METHOD = 2

#######################################
#     PUNISH METHOD 0 - CONFIG        #
#######################################
WARNING_LVL0 = "Warning %s ! Do not use this weapon! Its forbidden!"


#######################################
#     PUNISH METHOD 1 - CONFIG        #
#######################################
WARNING_LVL1 = "Warning %s ! You have been killed for using restricted weapon!"


#######################################
#     PUNISH METHOD 2 - CONFIG        #
#######################################
HOW_MANY_KILLS_TO_KICK = 2
WARNING_AFTER_FRAG = "Warning %s ! This weapon is forbidden! Stop being a n00b or you will get kicked!"
RESTRICTED_WEAPON_KICK_MSG = "Kicking %s for using restricted weapons!"
RESTRICTED_WEAPON_KICK_REASON = "You have been kicked for using restricted weapons!"
RESTRICTED_WEAPON_KICK_IN_MINUTES = 10


#####################
#   ANTI COMMANDER  #
#############################################################################################################
# Here you can enable or disable commander protection.                                                      #
# Module can be enabled with ANTICOMMANDER set to 1. Use 0 to disable it.                                   #
# Warning can be set in COMMANDER_MSG (put %s for player name)                                              #
#                                                                                                           #
# Instead of 'only info' you can enable commander kicking by switching COMMANDER_AUTOKICK to 1              #
# Then you can set other things:                                                                            #
#                                                                                                           #
# COMMANDER_KICK_TIME_IN_MINUTES - For how long commander should be kicked out?                             #
#                                                                                                           #
# COMMANDER_KICK_MSG - This msg appears in game when script is kicking commander (put %s for player name)   #
#                                                                                                           #
# COMMANDER_KICK_REASON - This msg gets player after kick - of course in cool punkbuster window ;)          #
#############################################################################################################
ANTICOMMANDER = 0
COMMANDER_MSG = "Warning! Player %s became a commander!"

COMMANDER_AUTOKICK = 0
COMMANDER_KICK_TIME_IN_MINUTES = 2
COMMANDER_KICK_MSG = "Kicking %s for using commander!"
COMMANDER_KICK_REASON = "You have been kicked for using commander!"

######################
#   ADMIN SETTINGS   #
###########################################################################################
# Here you can set new admin(s) for rcon administration of this script.                   #
# Just put his/her name in " " (dont forget about prefix!). Add comma if more then one ;] #
# example: ADMIN_LIST = "[V!S] MisiekBest[PL]", "#SOF# FrYzJeR.inf"                        #
###########################################################################################
ADMIN_LIST = "[V!S] MisiekBest[PL]", "#NM# MisiekBest[PL]"




################################################################################
################################################################################
##->                     END OF GLOBAL CONFIGURATION                        <-##
##->                    DONT CHANGE ANYTHING BELOW ;)                       <-##
################################################################################
################################################################################




















import bf2
import host
_MED_ONLY_FW_ = "usrif_m4","usrif_m24","usrif_m203","uslmg_m249saw","usrif_remington11-87","usrif_mp5_a3","usrgl_m203","usatp_predator","c4_explosives","usmin_claymore","at_mine","rurrif_ak74u","rurif_dragunov","rurif_gp30","rulmg_rpk74","rusht_saiga12","rurif_bizon","rurgl_gp30","chat_eryx","chrif_type95","chsni_type88","rurif_gp25","chlmg_type95","chsht_norinco982","chrif_type85","rurgl_gp25","usrif_g36c","ussni_m95_barret","usrif_g3a3","rulmg_pkm","ussht_jackhammer","chsht_protecta","usrif_fnscarl","gbrif_l96a1","sasrif_fn2000","sasgr_fn2000","sasrif_mg36","sasrif_mp7","eurif_fnp90"
_MED_ONLY_NO_UN_FW_ = "usrif_m4","usrif_m24","usrif_m203","uslmg_m249saw","usrif_remington11-87","usrif_mp5_a3","usrgl_m203","usatp_predator","c4_explosives","usmin_claymore","at_mine","rurrif_ak74u","rurif_dragunov","rurif_gp30","rulmg_rpk74","rusht_saiga12","rurif_bizon","rurgl_gp30","chat_eryx","chrif_type95","chsni_type88","rurif_gp25","chlmg_type95","chsht_norinco982","chrif_type85","rurgl_gp25","usrif_g36c","ussni_m95_barret","usrif_g3a3","rulmg_pkm","ussht_jackhammer","chsht_protecta","usrif_fnscarl","gbrif_l96a1","sasrif_fn2000","sasgr_fn2000","sasrif_mg36","sasrif_mp7","eurif_fnp90","usrif_sa80","sasrif_g36e"
_KPS_ONLY_AW_ = "kni_knife","uspis_92fs_silencer","uspis_92fs","rupis_baghira_silencer","rupis_baghira","chpis_qsz92_silencer","chpis_qsz92"
_NO_UNLOCKS_FW_ = "usrif_g36c","ussni_m95_barret","usrif_g3a3","rulmg_pkm","ussht_jackhammer","usrif_sa80","chsht_protecta","usrif_fnscarl","gbrif_l96a1","sasrif_fn2000","sasgr_fn2000","sasrif_mg36","sasrif_mp7","sasrif_g36e","eurif_fnp90"
_NO_SNIPERS_ = "usrif_m24","rurif_dragunov","chsni_type88", "ussni_m95_barret", "gbrif_l96a1"
playerKickList = []
def init():
	global OLDSCHOOL_LEVEL, PUNISH_METHOD, ANTICOMMANDER
	if (OLDSCHOOL_LEVEL != 0):
		if (ANTICOMMANDER == 1): host.registerHandler('ChangedCommander', onCommander, 1)
		if (PUNISH_METHOD == 2): host.registerHandler('PlayerKilled', onPlayerKilled, 1)
		if (PUNISH_METHOD == 0 or (PUNISH_METHOD == 1 and OLDSCHOOL_LEVEL != 3)): host.registerHandler('PlayerChangeWeapon', onPlayerChangeWeapon, 1)
		host.registerHandler('RemoteCommand', onRemoteCommand, 1)
		host.registerGameStatusHandler(onGameStatusChange)
		host.rcon_invoke('echo "bf2_oldschool.py by MisiekBest loaded"')
	else:
		host.rcon_invoke('echo "bf2_oldschool.py by MisiekBest loaded, script DISABLED by config!"')

def onCommander(teamid, oldCommanderPlayerObject, player):
		global OLDSCHOOL_LEVEL
		if (OLDSCHOOL_LEVEL != 0):	
			global ANTICOMMANDER
			if (ANTICOMMANDER): #yeap. Double check. Unfortunately DICE forgot to implement host.UNregisterHandler... And this is the only way to disable anticommander (and other) 'on the fly' by using remote rcon command. Sorry :P
				global COMMANDER_AUTOKICK
				if (COMMANDER_AUTOKICK == 1):
					global COMMANDER_KICK_MSG, COMMANDER_KICK_REASON, COMMANDER_KICK_TIME_IN_MINUTES
					host.sgl_sendTextMessage( 0, 12, 1, str(COMMANDER_KICK_MSG)  % (player.getName()), 0)
					host.rcon_invoke("pb_sv_kick \""+str(player.getName())+"\" "+str(COMMANDER_KICK_TIME_IN_MINUTES)+" \""+str(COMMANDER_KICK_REASON)+"\"")
				else:
					global COMMANDER_MSG
					host.sgl_sendTextMessage( 0, 12, 1, str(COMMANDER_MSG)  % (player.getName()), 0)
					host.sgl_sendTextMessage( 0, 12, 1, str(COMMANDER_MSG)  % (player.getName()), 0)
					host.sgl_sendTextMessage( 0, 12, 1, str(COMMANDER_MSG)  % (player.getName()), 0)
					host.sgl_sendTextMessage( 0, 12, 1, str(COMMANDER_MSG)  % (player.getName()), 0)
					host.sgl_sendTextMessage( 0, 12, 1, str(COMMANDER_MSG)  % (player.getName()), 0)

def onPlayerKilled(victim, attacker, weapon, assists, victimSoldierObject):
	global OLDSCHOOL_LEVEL
	if (OLDSCHOOL_LEVEL != 0):
		global PUNISH_METHOD
		if (PUNISH_METHOD == 2):
			global NO_C4, NO_CLAYMORE, NO_MOUNTED_MGS, NO_TOW_MISSILE
			if OLDSCHOOL_LEVEL == 1:
				global _MED_ONLY_FW_
				checkAndJudge(_MED_ONLY_FW_,attacker,weapon,0)
			elif OLDSCHOOL_LEVEL == 2:
				global _MED_ONLY_NO_UN_FW_
				checkAndJudge(_MED_ONLY_NO_UN_FW_,attacker,weapon,0)
			elif OLDSCHOOL_LEVEL == 3:
				global _KPS_ONLY_AW_
				checkAndJudge(_KPS_ONLY_AW_,attacker,weapon,1)
			elif OLDSCHOOL_LEVEL == 4:
				global _NO_UNLOCKS_FW_
				checkAndJudge(_NO_UNLOCKS_FW_,attacker,weapon,0)
			elif OLDSCHOOL_LEVEL == 5:
				pass
			elif OLDSCHOOL_LEVEL == 6:
				global _NO_SNIPERS_
				checkAndJudge(_NO_SNIPERS_,attacker,weapon,0)
			else:
				pass
				
				
			if NO_C4 or NO_CLAYMORE or NO_MOUNTED_MGS or NO_TOW_MISSILE: checkAndJudgeMisc(attacker, weapon)


def onPlayerChangeWeapon(player, oldWeapon, weapon):
	global OLDSCHOOL_LEVEL, PUNISH_METHOD
	if (OLDSCHOOL_LEVEL != 0):
		if (PUNISH_METHOD == 0 or (PUNISH_METHOD == 1 and OLDSCHOOL_LEVEL != 3)):	
			global NO_C4, NO_CLAYMORE, NO_MOUNTED_MGS, NO_TOW_MISSILE
			if OLDSCHOOL_LEVEL == 1:
				global _MED_ONLY_FW_
				changedWeapon(_MED_ONLY_FW_,player,weapon,0)
			elif OLDSCHOOL_LEVEL == 2:
				global _MED_ONLY_NO_UN_FW_
				changedWeapon(_MED_ONLY_NO_UN_FW_,player,weapon,0)
			elif OLDSCHOOL_LEVEL == 3:
				global _KPS_ONLY_AW_
				changedWeapon(_KPS_ONLY_AW_,player,weapon,1)
			elif OLDSCHOOL_LEVEL == 4:
				global _NO_UNLOCKS_FW_
				changedWeapon(_NO_UNLOCKS_FW_,player,weapon,0)
			elif OLDSCHOOL_LEVEL == 5:
				pass
			elif OLDSCHOOL_LEVEL == 6:
				global _NO_SNIPERS_
				changedWeapon(_NO_SNIPERS_,player,weapon,0)
			else:
				pass
				
				
			if NO_C4 or NO_CLAYMORE or NO_MOUNTED_MGS or NO_TOW_MISSILE: changedWeaponMisc(player, weapon)


def sayAll(msg):
	host.rcon_invoke("game.sayAll \"" + str(msg) + "\"")
	

def onRemoteCommand(playerId, cmd):
	playerObject =  bf2.playerManager.getPlayerByIndex(playerId)
	playerName = playerObject.getName()
	global ADMIN_LIST
	if (str(playerName) in ADMIN_LIST):
		execRconCmd(cmd)
	
def checkAndJudge(WeaponList,attacker,weapon,method):
	if not (method):
		if (str(weapon.templateName) in WeaponList): KickerSystem(attacker)
	else:
		if not (str(weapon.templateName) in WeaponList): KickerSystem(attacker)

def checkAndJudgeMisc(attacker, weapon):
	global NO_C4, NO_CLAYMORE, NO_MOUNTED_MGS, NO_TOW_MISSILE
	if ((NO_CLAYMORE and weapon.templateName == "usmin_claymore") or (NO_C4 and weapon.templateName == "c4_explosives") or (NO_MOUNTED_MGS and weapon.templateName == "rulmg_rpk74_stationary") or (NO_TOW_MISSILE and weapon.templateName == "ats_hj8_Launcher")): KickerSystem(attacker)
	
def KickerSystem(player):
	global playerKickList, HOW_MANY_KILLS_TO_KICK, RESTRICTED_WEAPON_KICK_MSG, RESTRICTED_WEAPON_KICK_REASON, WARNING_AFTER_FRAG, RESTRICTED_WEAPON_KICK_IN_MINUTES
	playerId = player.getProfileId()
	t = 0
	for temp_player in playerKickList:
		if (int(playerId) == int(temp_player[0])):
			temp_player[1]+=1;
			if (temp_player[1] >= HOW_MANY_KILLS_TO_KICK):
				host.sgl_sendTextMessage( 0, 12, 1, str(RESTRICTED_WEAPON_KICK_MSG)  % (player.getName()), 0)
				host.rcon_invoke("pb_sv_kick \""+str(player.getName())+"\" "+str(RESTRICTED_WEAPON_KICK_IN_MINUTES)+" \""+str(RESTRICTED_WEAPON_KICK_REASON)+"\"")
				del playerKickList[playerKickList.index([playerId,temp_player[1]])]
				t = 1
				
			else:
				host.sgl_sendTextMessage( 0, 12, 1, str(WARNING_AFTER_FRAG)  % (player.getName()), 0)
				t = 1
			
	if not (t): 
		playerKickList.append([playerId, 1])
		host.sgl_sendTextMessage( 0, 12, 1, str(WARNING_AFTER_FRAG)  % (player.getName()), 0)
		t = 0
def changedWeapon(WeaponList, player, weapon, method):
	global PUNISH_METHOD, WARNING_LVL0, WARNING_LVL1
	if not (method):
		if (str(weapon.templateName) in WeaponList):
			if not (PUNISH_METHOD):
				host.sgl_sendTextMessage( 0, 12, 1, str(WARNING_LVL0)  % (player.getName()), 0)
			else:
				player.getDefaultVehicle().setDamage(0)
				host.sgl_sendTextMessage( 0, 12, 1, str(WARNING_LVL1)  % (player.getName()), 0)
	else:
		if not (str(weapon.templateName) in WeaponList):
			if not (PUNISH_METHOD):
				host.sgl_sendTextMessage( 0, 12, 1, str(WARNING_LVL0)  % (player.getName()), 0)
			else:
				player.getDefaultVehicle().setDamage(0)
				host.sgl_sendTextMessage( 0, 12, 1, str(WARNING_LVL1)  % (player.getName()), 0)
	
def changedWeaponMisc(player, weapon):
	global NO_C4, NO_CLAYMORE, NO_MOUNTED_MGS, NO_TOW_MISSILE, PUNISH_METHOD, WARNING_LVL0, WARNING_LVL1
	if ((NO_CLAYMORE and weapon.templateName == "usmin_claymore") or (NO_C4 and weapon.templateName == "c4_explosives") or (NO_MOUNTED_MGS and weapon.templateName == "rulmg_rpk74_stationary") or (NO_TOW_MISSILE and weapon.templateName == "ats_hj8_Launcher")):
		if not (PUNISH_METHOD):
			host.sgl_sendTextMessage( 0, 12, 1, str(WARNING_LVL0)  % (player.getName()), 0) 
		else:
			player.getDefaultVehicle().setDamage(0)
			host.sgl_sendTextMessage( 0, 12, 1, str(WARNING_LVL1)  % (player.getName()), 0)
			
def isThirdArg(sc):
	try:
		if (sc[0] and sc[1] and sc[2]):
			return True
	except IndexError:
		return False
		
def isInt(expression):
	try:
		int(expression)
		return True
	except ValueError:
		return False
		
def execRconCmd(cmd):
	sc = str(cmd).split()
	if (sc[0] == "bfo"):
		if not (isThirdArg(sc)):
			if (sc[1] == "status"):
				global RESTRICTED_WEAPON_KICK_IN_MINUTES, HOW_MANY_KILLS_TO_KICK, OLDSCHOOL_LEVEL, NO_C4, NO_CLAYMORE, NO_MOUNTED_MGS, NO_TOW_MISSILE, PUNISH_METHOD, ANTICOMMANDER, COMMANDER_AUTOKICK, COMMANDER_KICK_TIME_IN_MINUTES
				host.rcon_invoke("game.sayAll \"MAIN CONFIG ==> OLDSCHOOL LEVEL: " + str(OLDSCHOOL_LEVEL) + ", PUNISH METHOD: " + str(PUNISH_METHOD) + ", NO CLAYMORE: " + str(NO_CLAYMORE) + ", NO C4: " + str(NO_C4) + ", NO MOUNTED MGS: " + str(NO_MOUNTED_MGS) + ", NO TOW: " + str(NO_TOW_MISSILE) + "\"")
				host.rcon_invoke("game.sayAll \"PUNISH METHOD 2 KICKER SYSTEM ==>  HOW MANY KILLS TO KICK: " + str(HOW_MANY_KILLS_TO_KICK) + ", RESTRICTED WEAPON KICK TIME: " + str(NO_C4) + "min.\"")
				host.rcon_invoke("game.sayAll \"ANTICOMM ==> ANTICOMMANDER: " + str(ANTICOMMANDER) + ", COMMANDER AUTOKICK: " + str(COMMANDER_AUTOKICK) + ", COMMANDER KICK TIME: " + str(COMMANDER_KICK_TIME_IN_MINUTES) + "min.\"")
			elif (sc[1] == "punish"):
				global PUNISH_METHOD
				host.rcon_invoke("game.sayAll \"BFO:::      PUNISH METHOD: " + str(PUNISH_METHOD) + "\"")
			elif (sc[1] == "olevel"):
				global OLDSCHOOL_LEVEL
				host.rcon_invoke("game.sayAll \"BFO:::      OLDSCHOOL LEVEL: " + str(OLDSCHOOL_LEVEL) + "\"")
			elif (sc[1] == "c4"):
				global NO_C4
				host.rcon_invoke("game.sayAll \"BFO:::      NO C4: " + str(NO_C4) + "\"")
			elif (sc[1] == "claymore"):
				global NO_CLAYMORE
				host.rcon_invoke("game.sayAll \"BFO:::      NO CLAYMORE: " + str(NO_CLAYMORE) + "\"")
			elif (sc[1] == "mgs"):
				global NO_MOUNTED_MGS
				host.rcon_invoke("game.sayAll \"BFO:::      NO MOUNTED MGS: " + str(NO_MOUNTED_MGS) + "\"")
			elif (sc[1] == "tow"):
				global NO_TOW_MISSILE
				host.rcon_invoke("game.sayAll \"BFO:::      NO TOW MISSILE: " + str(NO_TOW_MISSILE) + "\"")
			elif (sc[1] == "kick_frags"):
				global HOW_MANY_KILLS_TO_KICK
				host.rcon_invoke("game.sayAll \"BFO:::      KICK PLAYER AFTER: " + str(HOW_MANY_KILLS_TO_KICK) + " FRAGS.\"")
			elif (sc[1] == "kick_time"):
				global RESTRICTED_WEAPON_KICK_IN_MINUTES
				host.rcon_invoke("game.sayAll \"BFO:::      KICK PLAYER FOR: " + str(RESTRICTED_WEAPON_KICK_IN_MINUTES) + " MIN.\"")
			elif (sc[1] == "anticomm"):
				global ANTICOMMANDER
				host.rcon_invoke("game.sayAll \"BFO:::      ANTI COMMANDER: " + str(ANTICOMMANDER) + "\"")
			elif (sc[1] == "commkick"):
				global COMMANDER_AUTOKICK
				host.rcon_invoke("game.sayAll \"BFO:::      COMMANDER AUTOKICKER: " + str(COMMANDER_AUTOKICK) + "\"")
			elif (sc[1] == "commkick_time"):
				global COMMANDER_KICK_TIME_IN_MINUTES
				host.rcon_invoke("game.sayAll \"BFO:::      KICK COMMANDER FOR: " + str(COMMANDER_KICK_TIME_IN_MINUTES) + " MIN.\"")
			elif (sc[1] == "help"):
				sayAll("                             Ver 0.9 BETA Last changed: 25.Apr.2008")
				sayAll("                             For more info mail to: misiekbest@misiekbest.pl or visit website: http://bfo.misiekbest.pl")
				sayAll("This help include all commands that can be executed in game console via rcon.")
				sayAll("TO EXECUTE COMMAND TYPE IN CONSOLE: rcon bfo [command] [value].")
				sayAll("")
				sayAll("############## OLDSCHOOL LEVEL ##############")
				sayAll("#############################################")
				sayAll("olevel         # Return number of oldschool level")
				sayAll("olevel [value] # Set oldschool level to given value")
				sayAll("Here are all oldschool levels:")
				sayAll("0 - Scrpit completely disabled.")
				sayAll("1 - ONLY MEDICS and MEDICS UNLOCKS")
				sayAll("2 - ONLY MEDICS and NO MEDICS UNLOCKS")
				sayAll("3 - ONLY KNIFE, PISTOL AND SHOCK PADDLES ALLOWED. NOTE: This level will only work with punish method set to 0 or 2")
				sayAll("4 - NO UNLOCKS")
				sayAll("5 - DONT USE OLDSCHOOL LEVEL, JUST CHECK OTHER THINGS LIKE NO C4 or NO CLAYMORE")
				sayAll("6 - NO SNIPERS")
				sayAll("")
				sayAll("############## PUNISH METHOD  ##############")
				sayAll("############################################")
				sayAll("punish         # Return number of punish method")
				sayAll("punish [value] # Set punish method to given value")
				sayAll("Here are all punish methods:")
				sayAll("0 - Only warning enabled. No other punishment")
				sayAll("1 - Kill player just after respawn with forbidden weapon. If restricted are c4 or claymore player will die after switching to them. This wont work for mounted mgs and tow. Sorry.")
				sayAll("2 - Kick player after previously given kick_frags variable. To set number of frags run: rcon bfo kick_frags [value]")
				sayAll("")
				sayAll("##############   MISC WEAPONS   ##############")
				sayAll("##############################################")
				sayAll("c4         # Return status of C4 restriction")
				sayAll("c4 [value] # Enable or disble C4 restriction. 0-Disable  1-Enable")
				sayAll("claymore         # Return status of CLAYMORE restriction")
				sayAll("claymore [value] # Enable or disble CLAYMORE restriction. 0-Disable  1-Enable")
				sayAll("mgs         # Return status of MOUNTED MGS restriction")
				sayAll("mgs [value] # Enable or disble MOUNTED MGS restriction. 0-Disable  1-Enable")
				sayAll("tow         # Return status of TOW MISSILE restriction")
				sayAll("tow [value] # Enable or disble TOW MISSILE restriction. 0-Disable  1-Enable")
				sayAll("")
				sayAll("##############   KICKER SYSTEM (punish 2)   ##############")
				sayAll("##########################################################")
				sayAll("kick_frags         # Return number of how many kills from restricted weapon to kick player")
				sayAll("kick_frags [value] # Set HOW_MANY_KILLS_TO_KICK to given value")
				sayAll("kick_time          # Return minutes for how long player should be kicked out.")
				sayAll("kick_time [value]  # Set minutes for how long player should be kicked out.")
				sayAll("")
				sayAll("##############    ANTI COMMANDER    ##############")
				sayAll("##################################################")
				sayAll("anticomm           # Return status of ANTICOMMANDER system")
				sayAll("anticomm [value]   # Enable or disble commander restriction. 0-Disable  1-Enable")
				sayAll("commkick           # Return status of COMMANDER KICKER system")
				sayAll("commkick [value]   # Enable or disble commander kicking. 0-Disable  1-Enable")
				sayAll("commkick_time          # Return minutes for how long commander should be kicked out.")
				sayAll("commkick_time [value]  # Set minutes for how long commander should be kicked out.")
				sayAll("")
				sayAll("")
				sayAll("")
				sayAll("")
				sayAll("HELP GENERATED. NOW OPEN YOUR CONSOLE TO SEE IT. YOU CAN NAVIGATE UP AND DOWN BY PRESSING PAGE UP AND PAGE DOWN ON YOUR KEYBOARD")
			else:
				host.rcon_invoke("game.sayAll \"BFO:::      !!!!ERROR!!!! Unknown command : " + str(sc[1]) + "\"")
				host.rcon_invoke("game.sayAll \"BFO:::      Use: status, punish, olevel, c4, claymore, mgs, tow, kick_frags, kick_time, anticomm, commkick, commkick_time\"")
		else:
			if (isInt(sc[2])):
				if (sc[1] == "punish"):
					if (0<=int(sc[2])<=2):
						global PUNISH_METHOD
						PUNISH_METHOD = int(sc[2])
						if (PUNISH_METHOD == 0 or PUNISH_METHOD == 1):
							try:
								host.registerHandler('PlayerChangeWeapon', onPlayerChangeWeapon, 1)
							except:
								pass
						else:
							try:
								host.registerHandler('PlayerKilled', onPlayerKilled, 1)
							except:
								pass
						host.rcon_invoke("game.sayAll \"BFO:::      PUNISH METHOD SET TO: " + str(sc[2]) + "\"")
					else:
						sayAll("BFO:::      !!!!ERROR!!!! Punish method must be 0, 1 or 2 ")
				elif (sc[1] == "olevel"):
					if (0<=int(sc[2])<=6):
						global OLDSCHOOL_LEVEL
						OLDSCHOOL_LEVEL = int(sc[2])
						host.rcon_invoke("game.sayAll \"BFO:::      OLDSCHOOL LEVEL SET TO: " + str(sc[2]) + "\"")
					else:
						sayAll("BFO:::      !!!!ERROR!!!! oldschool level must be 0, 1, 2, 3, 4, 5 or 6")
				elif (sc[1] == "c4"):
					if (0<=int(sc[2])<=1):
						global NO_C4
						NO_C4 = int(sc[2])
						host.rcon_invoke("game.sayAll \"BFO:::      NO C4 SET TO: " + str(sc[2]) + "\"")
					else:
						sayAll("BFO:::      !!!!ERROR!!!! C4 can be set only to 0 or 1")
				elif (sc[1] == "claymore"):
					if (0<=int(sc[2])<=1):
						global NO_CLAYMORE
						NO_CLAYMORE = int(sc[2])
						host.rcon_invoke("game.sayAll \"BFO:::      NO CLAYMORE SET TO: " + str(sc[2]) + "\"")
					else:
						sayAll("BFO:::      !!!!ERROR!!!! CLAYMORE can be set only to 0 or 1")
				elif (sc[1] == "mgs"):
					if (0<=int(sc[2])<=1):
						global NO_MOUNTED_MGS
						NO_MOUNTED_MGS = int(sc[2])
						host.rcon_invoke("game.sayAll \"BFO:::      NO MOUNTED MGS SET TO: " + str(sc[2]) + "\"")
						sayAll("BFO:::      !!!!ERROR!!!! MGS can be set only to 0 or 1")
				elif (sc[1] == "tow"):
					if (0<=int(sc[2])<=1):
						global NO_TOW_MISSILE
						NO_TOW_MISSILE = int(sc[2])
						host.rcon_invoke("game.sayAll \"BFO:::      NO TOW MISSILE SET TO: " + str(sc[2]) + "\"")
					else:
						sayAll("BFO:::      !!!!ERROR!!!! TOW can be set only to 0 or 1")
				elif (sc[1] == "kick_frags"):
					if (0<=int(sc[2])):
						global HOW_MANY_KILLS_TO_KICK
						HOW_MANY_KILLS_TO_KICK = int(sc[2])
						host.rcon_invoke("game.sayAll \"BFO:::      HOW MANY KILLS TO KICK SET TO: " + str(sc[2]) + " FRAGS\"")
					else:
						sayAll("BFO:::      !!!!ERROR!!!! KICK_FRAGS must be greater than or equal to 0")
				elif (sc[1] == "kick_time"):
					if (0<=int(sc[2])):
						global RESTRICTED_WEAPON_KICK_IN_MINUTES
						RESTRICTED_WEAPON_KICK_IN_MINUTES = int(sc[2])
						host.rcon_invoke("game.sayAll \"BFO:::      KICK PLAYER TIME SET TO: " + str(sc[2]) + " MIN.\"")
					else:
						sayAll("BFO:::      !!!!ERROR!!!! KICK_TIME must be greater than or equal to 0")
				elif (sc[1] == "anticomm"):
					if (0<=int(sc[2])<=1):
						global ANTICOMMANDER
						ANTICOMMANDER = int(sc[2])
						if (ANTICOMMANDER == 1):
							try:
								host.registerHandler('ChangedCommander', onCommander, 1)
							except:
								pass
						host.rcon_invoke("game.sayAll \"BFO:::      ANTI COMMANDER SET TO: " + str(sc[2]) + "\"")
					else:
						sayAll("BFO:::      !!!!ERROR!!!! ANTICOMM can be set only to 0 or 1")
				elif (sc[1] == "commkick"):
					if (0<=int(sc[2])<=1):
						global COMMANDER_AUTOKICK
						COMMANDER_AUTOKICK = int(sc[2])
						host.rcon_invoke("game.sayAll \"BFO:::      COMMANDER AUTOKICK SET TO: " + str(sc[2]) + "\"")
					else:
						sayAll("BFO:::      !!!!ERROR!!!! COMMKICK can be set only to 0 or 1")
				elif (sc[1] == "commkick_time"):
					if (0<=int(sc[2])):
						global COMMANDER_KICK_TIME_IN_MINUTES
						COMMANDER_KICK_TIME_IN_MINUTES = int(sc[2])
						host.rcon_invoke("game.sayAll \"BFO:::      COMMANDER KICK TIME SET TO: " + str(sc[2]) + " MIN.\"")
					else:
						sayAll("BFO:::      !!!!ERROR!!!! COMMKICK_TIME must be greater than or equal to 0")
				else:
					host.rcon_invoke("game.sayAll \"BFO:::      !!!!ERROR!!!! Unknown command : " + str(sc[2]) + "\"")
					host.rcon_invoke("game.sayAll \"BFO:::      Use: punish, olevel, c4, claymore, mgs, tow, kick_frags, kick_time, anticomm, commkick, commkick_time\"")
			else:
				host.rcon_invoke("game.sayAll \"BFO:::      !!!!ERROR!!!! Third argument must be numerical ammount! You wrote: " + str(sc[2]) + "\"")
				

def onGameStatusChange(status):
	if (status == bf2.GameStatus.EndGame):
		global playerKickList
		playerKickList = []