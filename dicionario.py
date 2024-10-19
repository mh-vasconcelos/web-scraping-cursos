{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "from imports import *\n",
    "from main_ws import *"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 1 -  bs(requisicao, tipo da requisição)\n",
    "Aqui, usamos o req.text e depois 'html.parser' que funciona como indicador do tipo do primeiro argumento (html, no caso)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'bs' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[7], line 1\u001b[0m\n\u001b[1;32m----> 1\u001b[0m \u001b[43mbs\u001b[49m(req, \u001b[38;5;124m'\u001b[39m\u001b[38;5;124mhtml.parser\u001b[39m\u001b[38;5;124m'\u001b[39m)\n",
      "\u001b[1;31mNameError\u001b[0m: name 'bs' is not defined"
     ]
    }
   ],
   "source": [
    "bs(req, 'html.parser')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
