#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
BankAccount
============
Aquest mòdul conté la classe BankAccount la qual té els següents atributs:
    ======================== =========== ===================================================
    Atribut                  Tipus       Significat
    ======================== =========== ===================================================
    +id                      string      És l'identificador del compte (cadena de caràcters)
    +status                  boolean     És l'estat del compte: actiu o inactiu
    +balance                 float       És el saldo del compte
    +numDeposits             int         És el nombre d'ingressos mensuals
    +numWithdrawals          int         És el nombre de reintegraments mensuals
    +interestRate            float       És la taxa d'interès anual aplicable al compte
    +monthlyServiceCharges   float       És la comissió fixa mensual
    ======================== =========== ===================================================
=========
Funcions
=========
"""
import time


class BankAccount(object):

    def __guardarcompte(self):
        f1=open(self.id, "w")
        n=self.id+"&"+str(self.balance)+"&"+str(self.ianual)+"&"+str(self.carrega)
        f1.write(n+"\n")

    def split1(id):
        f1=open(id, "r")
        a=f.read()
        a=a.split("&")
        c=BankAccount(a[0],a[1],a[2],a[3])
        return c

    def __canviarstatus(self):
        self.status=self.balance>=25
    def __reinicialitzar(self):
        self.numWithdrawals=0
        self.numDeposits=0
    def __init__(self, id, balance, interestRate, monthlyServicesChange):
        self.ianual=interestRate
        self.id=id
        self.balance=balance
        self.__canviarstatus()
        self.numDeposits=0
        self.numWithdrawals=0
        self.carrega=monthlyServicesChange
        self.__guardarcompte()

    def withdraw(self, amount):
        """
        Retira diners del compte bancari
        >>> BA=BankAccount("ES6621000418401234567891", 30, 0.03, 3)
        >>> BA.withdraw(5)
        True
        >>> print BA.balance
        25
        >>> BA=BankAccount("ES6621000418401234567892", 10, 0.03, 3)
        >>> BA.withdraw(5)
        False
        >>> print BA.balance
        10
        """
        if self.status==False:
            return False
        else:
            self.balance-=amount
            self.numWithdrawals+=1
            self.__canviarstatus()
            self.__guardarcompte()
            return True

    def deposit(self, amount):
        """
        Afageix diners el compte si aquest supera la quantitat de 25 Euros canvia el seu estat a Actiu(true)
        >>> BA=BankAccount("ES6621000418401234567892", 10, 0.03, 3)
        >>> print BA.status
        False
        >>> BA.deposit(20)
        >>> print BA.status
        True
        >>> print BA.balance
        30
        """
        self.balance+=amount
        self.__canviarstatus()
        self.numDeposits+=1
        self.__guardarcompte()
    def __str__(self):
        """
        """
        if self.status:
            a="Deposits # ="+str(self.numDeposits)+" Withdrawals# ="+str(self.numWithdrawals)
        else:
            a="INACTIU"
        return "Data: "+ time.strftime("%X")+" "+time.strftime("%x")+"\n"+"CompteBancari: Codi IBAN: "+self.id[:4]+" Entitat: "+self.id[3:8]+" Oficina: "+self.id[8:12]+" num Compte: "+self.id[12:]+": "+str(float(self.balance))+" "+a

    def calcMonthlyInterest(self):
        """
        Calcula i ingressa l'interès mensual a abonar  en el compte, dividint per 12 l'interès anual aplicat i precedint a l'interès a la quantitat corresponent
        >>> c2=BankAccount("ES1000492352082414205416",10.0, 0.025, 5.0)
        >>> c2.calcMonthlyInterest()
        >>> print c2.balance
        10.0208333333
        """
        imensual=self.ianual/12.
        self.deposit(imensual*self.balance)

    def monthlyProcess(self):
        """
        Aplica al compte el procés mensual consistent en cobrar les comissions i pagar els interessos mesuals, d'acord
        amb la política de comissions explicada a l'enunciat i amb l'interés mensual dels interessos.
        També posa a zero els comptadors d'ingressos i reintegraments realitzats mensualment, preparant el comte per al nou mes.
        >>> c1=BankAccount("ES6621000418401234567891",100.0,0.03,2.5)
        >>> c1.deposit(0)
        >>> print c1.numDeposits
        1
        >>> c1.monthlyProcess()
        >>> print c1.balance
        97.74375
        >>> print c1.numDeposits
        0
        """
        n=0
        if self.numWithdrawals>4:
            n=self.numWithdrawals-4
        self.balance-=self.carrega
        self.calcMonthlyInterest()
        self.balance-=n
        self.__canviarstatus()
        self.__reinicialitzar()
        self.__guardarcompte()

def opcions():

    print "[0] Treure diners"
    print "[1] Ingressar diners"
    print "[2] Transferir diners"
    print "[3] Crear un compte"

    o= raw_input("Entri opció:")
    while o not in "0123":
        o=raw_input("Entri opcio correcte: ")
    return o

def menu():
    o=opcions()
    if o=="0":
        print "hola"
    elif o=="1":
        print "adeu"
    elif o=="2":
        print "quetal"
    elif o=="3":
        print "jeje"




if __name__ == "__main__":
    print "CAIXER AUTOMÀTIC"
    print
    try:
        a=open("hola", "r")
    except:
        print "hola"
    menu()
