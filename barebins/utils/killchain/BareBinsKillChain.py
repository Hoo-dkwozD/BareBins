#!/usr/bin/env python3

"""
:author: Hoo-dkwozD
:license: GPLv3
:version: 0.1
:date: 2025-05-23

List the kill chain stages and their descriptions.
Used to help categorise the modules in the exploit.

The default kill-chain provided is a simplified version 
of popular frameworks.
"""

# Python standard library imports
from enum import StrEnum

class KillChain(StrEnum):
    """
    Enum class for the kill chain stages.
    """
    
    RECON = "Reconnaissance of the target systems"
    WEAPON = "Weaponization of the payload"
    EXPLOIT = "Delivery of the payload & execution on the target"
    PERSIST = "Persistence on the target system"
    DISCOVERY = "Discovery of the target system for further exploitation"
    LATERAL = "Lateral movement within the target system"
    ESCALATE = "Privilege escalation on the target system"
    ACTION = "Action on Objectives of the target system"
