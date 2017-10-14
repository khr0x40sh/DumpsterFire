#!/usr/bin/python
#
# Filename:  
#
# Version: 1.0.0
#
# Author:  Joe Gervais (TryCatchHCF)
#
# Summary:
#
#
# Description:
#
#
# Example:
#
#

import os, sys

from FireModules.fire_module_base_class import *

class nmap_subnet_top_80_ports( FireModule ):

	def __init__(self):
		self.commentsStr = "NetworkScans/nmap_subnet_top_80_ports"
		return

	def __init__(self, moofStr):
		self.moofStr = moofStr
		self.commentsStr = "NetworkScans/nmap_subnet_top_80_ports"
		return

	def Description( self ):
		self.Description = "Runs nmap, probing Top 80 ports on all hosts of target network"
		return self.Description

        def Configure( self ):
                self.networkAddrStr = raw_input( "Enter Target Network IP Address (W.X.Y.Z): " )
                return

        def GetParameters( self ):
                return( self.networkAddrStr )

        def SetParameters( self, parametersStr ):
                self.networkAddrStr = parametersStr
                return

        def ActivateLogging( self, logFlag ):
                print self.commentsStr + ": Setting Logging flag!"
                print logFlag
                return

        def Ignite( self ):

                if ( self.networkAddrStr == "" ):
                        print "## ", self.commentsStr, ": Error - Network address string is blank"
                        return
		else:
			self.commandStr = "nmap -Pn -n --open -sT -sV --top-ports=80 " + self.networkAddrStr + "/24"
			print self.commentsStr + ": Scanning with " + self.commandStr
			os.system( self.commandStr )

		return

