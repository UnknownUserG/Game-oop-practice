# Import modules

import sys
import random
import math
import os
import getopt
import pygame
from socket import *
from pygame.locals import *
from random import shuffle


# Parent class for player and enemies
class Char:
    def __init__(self, hp, attack, magic, defence):
        self.hp = hp
        self.attack = attack
        self.magic = magic
        self.defence = defence

    # Display stats
    def showstats(self):
        print("HP " + str(self.hp) + " Attack " + str(self.attack) + " Magic " + str(self.magic) + " Defence " + str(
            self.defence))  # Enemies will override this function

    def takeDamage(self, dmg):
        self.hp -= dmg
        print("Player took " + str(dmg) + " damage!")
        print("Current HP: " + str(self.hp))


# Level = Determine max deck?
class Player(Char):
    def __init__(self, hp, attack, magic, defence, level):
        Char.__init__(self, hp, attack, magic, defence)
        self.level = level


class Enemy(Char):
    def __init__(self, hp, attack, magic, defence, level, name):
        Char.__init__(self, hp, attack, magic, defence)
        self.level = level
        self.name = name

    # Override
    def takeDamage(self, dmg):
        self.hp -= dmg
        print(self.name + " took " + str(dmg) + " damage!")
        print("Current HP: " + str(self.hp))


# id = card id
class Card:
    def __init__(self, id, name, hp, attack, shield):
        self.id = id
        self.name = name
        self.attack = attack
        self.shield = shield


# Build the card playing area
def buildCanvas():
    # Resolution
    window_width = 1024
    window_height = 768

    white = (255, 255, 255)
    black = (0, 0, 0)

    # Build stage
    pygame.init()
    gamedisplay = pygame.display.set_mode((window_width, window_height))
    gamedisplay.fill(white)
    pygame.display.update()

    # Build the deck and print it on the screen
    buildDeck(gamedisplay)


# Insert card id to draw the image -- Prototype
# printImage (card ID number, stage, xPos, yPos)
def printImage(id, gamedisplay, x, y):
    cardSizeX = 176
    cardSizeY = 250
    try:
        cardImg = pygame.image.load("assets/" + id + ".png")
        cardImg = pygame.transform.scale(cardImg, (cardSizeX, cardSizeY))
        gamedisplay.blit(cardImg, (x, y))
    # Catch pygame.error for the file import error
    except pygame.error:
        print("Card ID " + id + " not found!")


def buildDeck(gamedisplay):
    deck = ["009", "011", "020", "025", "028"]
    shuffle(deck)

    # I love myself
    for i in deck:
        printImage(i, gamedisplay, deck.index(i) * 150 + 100, 400)


# Main method, duh
def main():
    buildCanvas()

    crashed = False
    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True

        pygame.display.update()


main()
