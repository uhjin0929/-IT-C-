{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "private_outputs": true,
      "provenance": [],
      "collapsed_sections": [],
      "authorship_tag": "ABX9TyNaP/hjd7C7iU29dQETbqiB"
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "source": [
        "1."
      ],
      "metadata": {
        "id": "djL9jF91AcKN"
      }
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "MdXOQPFIAXyo"
      },
      "outputs": [],
      "source": [
        "house = input() #가구들의 사용량을 입력받구요\n",
        "house = house.split() #쪼개서 리스트로 만들어요\n",
        "house = list(map(int,house)) #원소들을 int로 바꿔요\n",
        "for i in house : \n",
        "    others = house.copy() # 깊은 복사\n",
        "    others.remove(i)\n",
        "    sum = 0\n",
        "    for j in others :\n",
        "        sum += j\n",
        "    sum /= len(others)\n",
        "    if i > (sum*1.5):\n",
        "        print(i) \n",
        "        break\n",
        "else :\n",
        "    print('Not Found')  \n",
        "\n"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "2."
      ],
      "metadata": {
        "id": "EYhynhGtCCXZ"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def TigerNumber(n):\n",
        "    n = str(n)\n",
        "    jarisu = []\n",
        "    for i in n:\n",
        "        jarisu.append(i)\n",
        "    n = int(n)\n",
        "    jarisu = list(map(int,jarisu))\n",
        "    for i in jarisu :\n",
        "        if n%i != 0 :\n",
        "            return False\n",
        "    else :\n",
        "        return True"
      ],
      "metadata": {
        "id": "l0uWwZXlCDUb"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "3."
      ],
      "metadata": {
        "id": "_2ZCCgn5AbJZ"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "a = input()\n",
        "a = list(map(int,a.split()))\n",
        "a.sort()\n",
        "b = input()\n",
        "b = list(map(int,b.split()))\n",
        "b.sort()\n",
        "if a == b :\n",
        "    print('YES')\n",
        "else : \n",
        "    print('NO')\n",
        "    \n"
      ],
      "metadata": {
        "id": "bCJDYoixFkq0"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "4. "
      ],
      "metadata": {
        "id": "ZOaMpvHGGuos"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "fourth = ['q','w','e','r','t','y','u','i','o','p']\n",
        "third = ['a','s','d','f','g','h','j','k','l']\n",
        "second = ['z','x','c','v','b','n','m']\n",
        "a = {}\n",
        "for i in fourth :\n",
        "    a[i] = 4\n",
        "for i in third :\n",
        "    a[i] = 3\n",
        "for i in second :\n",
        "    a[i] = 2\n",
        "a[' '] = 1\n",
        "sentence = input()\n",
        "sum = 0\n",
        "for x in range(len(sentence)-1) :\n",
        "    pirodo = a[sentence[x+1]] - a[sentence[x]]\n",
        "    if pirodo < 0 :\n",
        "        pirodo *= -1\n",
        "    sum += pirodo\n",
        "print(sum)\n",
        "    \n",
        "\n"
      ],
      "metadata": {
        "id": "X5IEplEkGv8n"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "1. (여기서부턴 계절)"
      ],
      "metadata": {
        "id": "KdmQK9aAJPXp"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "N = int(input())\n",
        "cola = N\n",
        "while N >= 3 :\n",
        "    newcola = N // 3\n",
        "    cola = cola + newcola\n",
        "    N = N % 3 + newcola \n",
        "print(cola)\n",
        "  \n"
      ],
      "metadata": {
        "id": "DrqObwzFJRKE"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "2."
      ],
      "metadata": {
        "id": "ORTVLiegMM0W"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "lst = []\n",
        "inilst = []\n",
        "breaker = False\n",
        "while True :\n",
        "    drink = input()\n",
        "    if drink == 'END':\n",
        "        break\n",
        "    lst.append(drink)\n",
        "for i in lst :\n",
        "    p = i.split()\n",
        "    initial = ''\n",
        "    for j in p :\n",
        "        initial += j[0]\n",
        "    inilst.append(initial)\n",
        "for i in range(len(inilst)) :\n",
        "    for j in range(i+1,len(inilst)):\n",
        "        if inilst[i] == inilst[j] :\n",
        "            print('YES')\n",
        "            breaker = True\n",
        "            break\n",
        "    if breaker :\n",
        "        break\n",
        "else :\n",
        "    print('NO')\n",
        "        \n",
        "\n",
        "    \n",
        "        \n",
        "    \n"
      ],
      "metadata": {
        "id": "bnhKT5QJMNuk"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "3."
      ],
      "metadata": {
        "id": "1zI8ynkYOpaf"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "infodict = {}\n",
        "while True :\n",
        "    info = input()\n",
        "    info = info.split()\n",
        "    if len(info) == 1:\n",
        "        print(infodict[info[0]])\n",
        "        break\n",
        "    if info[0] in infodict :\n",
        "        if infodict[info[0]] >= info[-1]:\n",
        "            infodict[info[0]] = info[-1]\n",
        "    else :\n",
        "        infodict[info[0]] = info[-1]"
      ],
      "metadata": {
        "id": "GIs4m8wTOqu2"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}