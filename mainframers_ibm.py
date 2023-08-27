
import time
import colorama
from threading import Timer
import json

colorama.init()

class SneakersInspiredRPG:
    def __init__(self):
        self.intro_text_color = "\033[1;36m"  # Cyan
        self.menu_text_color = "\033[1;33m"  # Yellow
        self.mission_text_color = "\033[1;32m"  # Green
        self.reset_color = "\033[0m"  # Reset to default
        self.current_room = "lobby"
        
    def color_print(self, color, text):
        print(f"{color}{text}{self.reset_color}")
        
    def introduction(self):
        self.color_print(self.intro_text_color, "A milosilo creation")
        time.sleep(2)
        self.color_print(self.intro_text_color, "More RPGs at github.com/milosilo")
        time.sleep(2)
        self.color_print(self.intro_text_color, "Follow @MiloSilo_Hacks for RPG releases and cybersecurity rants")
        time.sleep(2)
        self.color_print(self.intro_text_color, "=========================================================================")
        self.color_print(self.intro_text_color, "Welcome, Cyber Sleuth, to the IBM Mainframe CyberSec RPG!")
        self.color_print(self.intro_text_color, "=========================================================================")
        time.sleep(2)
        self.color_print(self.intro_text_color, "Your mission: Use your IBM mainframe cybersecurity skills to navigate dark and twisted maze of rooms and puzzles.")
        time.sleep(2)
        self.color_print(self.intro_text_color, "Are you ready?")
        time.sleep(2)
        self.main_menu()
        
    def main_menu(self):
        while True:
            self.color_print(self.menu_text_color, "Main Menu:")
            self.color_print(self.menu_text_color, "1. Start New Game")
            self.color_print(self.menu_text_color, "2. Load Saved Game")
            self.color_print(self.menu_text_color, "3. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.color_print(self.menu_text_color, "Starting a new game...")
                self.current_room = "Lobby"
                self.move_to_next_room()
                break
            elif choice == "2":
                try:
                    with open("saved_game.txt", "r") as f:
                        saved_data = json.load(f)
                    self.current_room = saved_data["current_room"]
                    self.color_print(self.menu_text_color, f"Loaded saved game. You are in {self.current_room}.")
                    self.move_to_next_room()
                    break
                except FileNotFoundError:
                    self.color_print(self.menu_text_color, "No saved game found. Starting a new game...")
                    self.current_room = "Lobby"
                    self.move_to_next_room()
                    break
                except json.JSONDecodeError:
                    self.color_print(self.menu_text_color, "Corrupted save file. Starting a new game...")
                    self.current_room = "Lobby"
                    self.move_to_next_room()
                    break
            elif choice == "3":
                self.color_print(self.menu_text_color, "Exiting the game. Goodbye!")
                exit(0)
            else:
                self.color_print(self.menu_text_color, "Invalid choice. Please try again.")
        
    def menu(self):
        while True:
            self.color_print(self.menu_text_color, f"You have entered the {self.current_room}.")
            self.color_print(self.menu_text_color, "1. Complete current room's mission")
            self.color_print(self.menu_text_color, "2. Save Game")
            self.color_print(self.menu_text_color, "3. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.complete_mission()
            elif choice == "2":
                with open("saved_game.txt", "w") as f:
                    json.dump({"current_room": self.current_room}, f)
                self.color_print(self.menu_text_color, "Game saved successfully.")
            elif choice == "3":
                self.color_print(self.menu_text_color, "Exiting the game. Goodbye!")
                exit(0)
            else:
                self.color_print(self.menu_text_color, "Invalid choice. Please try again.")
    
    def move_to_next_room(self):
        if self.current_room == "Lobby":
            self.current_room = "RACF_Room"
        elif self.current_room == "RACF_Room":
            self.current_room = "JCL_Room"
        elif self.current_room == "JCL_Room":
            self.current_room = "zos_Security_Room"
        elif self.current_room == "zos_Security_Room":
            self.current_room = "FTP_Security_Room"
        elif self.current_room == "FTP_Security_Room":
            self.current_room = "ESM_Configuration_Room"
        elif self.current_room == "ESM_Configuration_Room":
            self.current_room = "Encryption_Techniques_Room"
        elif self.current_room == "Encryption_Techniques_Room":
            self.current_room = "Incident_Response_Room"
        elif self.current_room == "Incident_Response_Room":
            self.current_room = "Final_Room"
        elif self.current_room == "Final_Room":
            self.current_room = "Game_Over"
        self.color_print(self.menu_text_color, f"You have moved to {self.current_room}.")
        self.complete_mission()

    def complete_mission(self):
        if self.current_room == "RACF_Room":
            self.mission_racf_management()
        elif self.current_room == "JCL_Room":
            self.mission_jcl_security()
        elif self.current_room == "zos_Security_Room":
            self.mission_zos_security()
        elif self.current_room == "FTP_Security_Room":
            self.mission_ftp_security()
        elif self.current_room == "ESM_Configuration_Room":
            self.ESM_Configuration_Room()
        elif self.current_room == "Encryption_Techniques_Room":
            self.mission_encryption_techniques()
        elif self.current_room == "Incident_Response_Room":
            self.mission_incident_response()
        elif self.current_room == "Final_Room":
            self.mission_final_room()
    
    # Mission Methods
    def mission_racf_management(self):
        self.color_print(self.mission_text_color, "You've entered a room that resembles a cybersecurity operations center.")
        time.sleep(2)
        self.color_print(self.mission_text_color, "Mission: Decrypt an encrypted message using RACF commands.")
        time.sleep(2)
        
        self.color_print(self.mission_text_color, "Before you is a mainframe terminal and a message encrypted in hex: 6D696C6F73696C6F2E636F6D")
        time.sleep(2)

        while True:
            self.color_print(self.mission_text_color, "Task 1: Type the RACF command to refresh a dataset access list.(SETROPTS RACLIST(DATASET) REFRESH)")
            answer1 = input()
            if answer1.upper() == "SETROPTS RACLIST(DATASET) REFRESH":
                self.color_print(self.mission_text_color, "Correct! Part of the encrypted message becomes clear: milos...")
                time.sleep(2)
                break
            else:
                self.color_print(self.mission_text_color, "Incorrect. Try again.")
                time.sleep(2)

        while True:
            self.color_print(self.mission_text_color, "Task 2: Type the RACF command to add a user to a group.(ADDUSER USERID(GROUP))")
            answer2 = input()
            if answer2.upper() == "ADDUSER USERID(GROUP)":
                self.color_print(self.mission_text_color, "Correct! The entire message is decrypted: milosilo.com")
                self.color_print(self.mission_text_color, "You've successfully decrypted the message. Move to the next room.")
                self.current_room = "JCL_Room"
                time.sleep(2)
                self.menu()
                break
            else:
                self.color_print(self.mission_text_color, "Incorrect. Try again.")
                time.sleep(2)

    def mission_jcl_security(self):
        self.color_print(self.mission_text_color, "You've entered a room filled with mainframe consoles and a giant screen showing a security wall.")
        time.sleep(2)
        self.color_print(self.mission_text_color, "Mission: Bypass the security wall using JCL (Job Control Language) skills.")
        time.sleep(2)
        
        self.color_print(self.mission_text_color, "You find a console ready for JCL input and a series of locked doors ahead.")
        time.sleep(2)
        self.color_print(self.mission_text_color, "Task 1: Type the JCL command to allocate 4M of memory for a program.(// EXEC PGM=IEFBR14,REGION=4M)")
        answer1 = input()
        if answer1.upper() == "// EXEC PGM=IEFBR14,REGION=4M":
            self.color_print(self.mission_text_color, "Correct! The first door unlocks.")
            time.sleep(2)
            
            self.color_print(self.mission_text_color, "Task 2: Type the JCL statement to specify that the job uses the MSGCLASS X output class.(// JOB MSGCLASS=X)")
            answer2 = input()
            if answer2.upper() == "// JOB MSGCLASS=X":
                self.color_print(self.mission_text_color, "Correct! The second door unlocks.")
                self.color_print(self.mission_text_color, "You've successfully bypassed the security wall. Move to the next room.")
                self.current_room = "zos_Security_Room"
                time.sleep(2)
                self.menu()
            else:
                self.color_print(self.mission_text_color, "Incorrect. You need to complete the mission to move on.")
                time.sleep(2)
        else:
            self.color_print(self.mission_text_color, "Incorrect. You need to complete the mission to move on.")
            time.sleep(2)

    def mission_zos_security(self):
        self.color_print(self.mission_text_color, "You've encountered a locked vault door made entirely out of stainless steel.")
        time.sleep(2)
        self.color_print(self.mission_text_color, "Mission: Unlock the z/OS vault.")
        time.sleep(2)
        
        self.color_print(self.mission_text_color, "You find a z/OS terminal, a locked safe, and a ticking clock counting down from 5 minutes.")
        time.sleep(2)
        self.color_print(self.mission_text_color, "Task 1: Type the protocol used for secure communication in z/OS.(SSL/TLS)")
        answer1 = input()
        if answer1.upper() == "SSL/TLS":
            self.color_print(self.mission_text_color, "Correct! The clock pauses briefly, and a compartment of the safe clicks open.")
            time.sleep(2)
            
            self.color_print(self.mission_text_color, "Task 2: Type the command to enable SAF (Security Authorization Facility) in z/OS.(S SAF,START)")
            answer2 = input()
            if answer2.upper() == "S SAF,START":
                self.color_print(self.mission_text_color, "Correct! The keypad beeps and a second compartment opens, revealing a key card.")
                time.sleep(2)

                self.color_print(self.mission_text_color, "Task 3: What z/OS utility would you use to encrypt the data at rest?(DFSMS)")
                answer3 = input()
                if answer3.upper() == "DFSMS":
                    self.color_print(self.mission_text_color, "Correct! The safe door swings open fully, revealing its contents.")
                    self.color_print(self.mission_text_color, "The vault is unlocked. Move to the next room.")
                    self.current_room = "FTP_Security_Room"
                    time.sleep(2)
                    self.menu()
                else:
                    self.color_print(self.mission_text_color, "Incorrect. You need to complete the mission to move on.")
                    time.sleep(2)
            else:
                self.color_print(self.mission_text_color, "Incorrect. You need to complete the mission to move on.")
                time.sleep(2)
        else:
            self.color_print(self.mission_text_color, "Incorrect. You need to complete the mission to move on.")
            time.sleep(2)
            
    def mission_ftp_security(self):
        self.color_print(self.mission_text_color, "You've entered a room resembling a data center, with the hum of servers filling the air.")
        time.sleep(2)
        self.color_print(self.mission_text_color, "Mission: Securely transfer a stolen file using FTPS on an IBM mainframe.")
        time.sleep(2)
        
        self.color_print(self.mission_text_color, "You find a mainframe terminal and an FTP client ready for a secure transfer.")
        time.sleep(2)
        self.color_print(self.mission_text_color, "Task 1: Type the FTP command to enter secure mode.(AUTH SSL)")
        answer1 = input()
        if answer1.upper() == "AUTH SSL":
            self.color_print(self.mission_text_color, "Correct! FTPS mode activated.")
            time.sleep(2)
            
            self.color_print(self.mission_text_color, "Task 2: Type the FTP command to set the data transfer mode to binary.(TYPE I)")
            answer2 = input()
            if answer2.upper() == "TYPE I":
                self.color_print(self.mission_text_color, "Correct! Data transfer mode set to binary.")
                self.color_print(self.mission_text_color, "The file is transferred securely. Move to the next room.")
                self.current_room = "ESM_Configuration_Room"
                time.sleep(2)
                self.menu()
            else:
                self.color_print(self.mission_text_color, "Incorrect. You need to complete the mission to move on.")
                time.sleep(2)
        else:
            self.color_print(self.mission_text_color, "Incorrect. You need to complete the mission to move on.")
            time.sleep(2)
    
    def ESM_Configuration_Room(self):
        self.color_print(self.mission_text_color, "\\nYou've entered a hacker's lair, filled with blueprints of mainframes.")
        time.sleep(2)
        self.color_print(self.mission_text_color, "Mission: Configure an External Security Manager (ESM) on an IBM mainframe.")
        time.sleep(2)
        
        self.color_print(self.mission_text_color, "You find an IBM mainframe console with ESM options.")
        time.sleep(2)
        self.color_print(self.mission_text_color, "Task 1: Type the name of the security manager you would use.(RACF)")
        answer1 = input()
        if answer1.upper() == "RACF":
            self.color_print(self.mission_text_color, "Correct! ESM chosen.")
            time.sleep(2)
            
            self.color_print(self.mission_text_color, "Task 2: Type the command to initialize RACF, if you chose RACF.(S RACF)")
            answer2 = input()
            if answer2.upper() == "S RACF":
                self.color_print(self.mission_text_color, "Correct! RACF initialized.")
                self.color_print(self.mission_text_color, "ESM successfully configured. Move to the next room.")
                self.current_room = "Encryption_Techniques_Room"
                time.sleep(2)
                self.menu()
            else:
                self.color_print(self.mission_text_color, "Incorrect. You need to complete the mission to move on.")
                time.sleep(2)
        else:
            self.color_print(self.mission_text_color, "Incorrect. You need to complete the mission to move on.")
            time.sleep(2)
        
    def mission_encryption_techniques(self):
        self.color_print(self.mission_text_color, "\\nYou've entered a room with old IBM mainframes and a complex network of cables.")
        time.sleep(2)
        self.color_print(self.mission_text_color, "Mission: Decrypt a sensitive message stored in an IBM mainframe dataset using proper encryption techniques.")
        time.sleep(2)
        
        self.color_print(self.mission_text_color, "You find a sticky note that says 'Decrypt with ICSF'.")
        time.sleep(2)
        self.color_print(self.mission_text_color, "Task 1: What command would you issue to enable ICSF?(S ICSF)")
        answer1 = input()
        if answer1.upper() == "S ICSF":
            self.color_print(self.mission_text_color, "Correct! ICSF is now enabled.")
            time.sleep(2)
            
            self.color_print(self.mission_text_color, "Task 2: Now, type the JCL code snippet to define a cryptographic key using ICSF.(//CSFPARM DD *)")
            answer2 = input()
            if answer2.upper() == "//CSFPARM DD *":
                self.color_print(self.mission_text_color, "Correct! You've defined a cryptographic key using ICSF.")
                self.color_print(self.mission_text_color, "The sensitive message is decrypted, revealing a password to the next room.")
                self.current_room = "Incident_Response_Room"
                time.sleep(2)
                self.menu()
            else:
                self.color_print(self.mission_text_color, "Incorrect. You need to complete the mission to move on.")
                time.sleep(2)
        else:
            self.color_print(self.mission_text_color, "Incorrect. You need to complete the mission to move on.")
            time.sleep(2)
            
    def mission_incident_response(self):
        self.color_print(self.mission_text_color, "\\nYou've entered a control room with multiple screens displaying real-time mainframe activity.")
        time.sleep(2)
        self.color_print(self.mission_text_color, "Mission: Identify and respond to a security incident on an IBM mainframe.")
        time.sleep(2)
        
        self.color_print(self.mission_text_color, "A red alert flashes on one of the screens, signaling a security incident.")
        time.sleep(2)
        self.color_print(self.mission_text_color, "Task 1: What is the first step in the incident response process according to the NIST framework?"(preparation))
        answer1 = input()
        if answer1.lower() == "preparation":
            self.color_print(self.mission_text_color, "Correct! You've acknowledged the first step.")
            time.sleep(2)
            
            self.color_print(self.mission_text_color, "Task 2: Type the z/OS command to display active jobs to identify any unusual activity.(D A)")
            answer2 = input()
            if answer2.upper() == "D A":
                self.color_print(self.mission_text_color, "Correct! You've displayed the active jobs and identified the rogue process.")
                self.color_print(self.mission_text_color, "You successfully contain the incident and secure the mainframe.")
                self.current_room = "Final_Room"
                time.sleep(2)
                self.menu()
            else:
                self.color_print(self.mission_text_color, "Incorrect. You need to complete the mission to move on.")
                time.sleep(2)
        else:
            self.color_print(self.mission_text_color, "Incorrect. You need to complete the mission to move on.")
            time.sleep(2)
        
    def timeout():
        print("Time's up! You've failed to complete the mission. Game Over.")
        exit(0)

    def mission_final_room(self):
        # Start the 2-minute timer
        t = Timer(120, self.timeout)
        t.start()

        self.color_print(self.mission_text_color, "\\nYou've entered the Final Room, a control center filled with blinking lights, encrypted codes, and a countdown clock.")
        time.sleep(2)
        self.color_print(self.mission_text_color, "Mission: Decrypt the ultimate encryption to save the mainframe within 2 minutes or the system will crash!")
        time.sleep(2)

        self.color_print(self.mission_text_color, "Before you, a mainframe terminal displays a series of encrypted messages: [A1B2C3], [D4E5F6], [G7H8I9].")
        time.sleep(2)
        self.color_print(self.mission_text_color, "Task 1: Type the RACF command to revoke access for a rogue user.(ALTUSER USERID(REVOKE))")
        answer1 = input()
        if answer1.upper() == "ALTUSER USERID(REVOKE)":
            self.color_print(self.mission_text_color, "Correct! The first encrypted message [A1B2C3] is decrypted to 'ACCESS'.")
            time.sleep(1)

            self.color_print(self.mission_text_color, "Task 2: Type the z/OS command to cancel a specific job ID. (e.g., C JOB1234)")
            answer2 = input()
            if answer2.upper().startswith("C JOB"):
                self.color_print(self.mission_text_color, "Correct! The second encrypted message [D4E5F6] is decrypted to 'DENIED'.")
                time.sleep(1)

                self.color_print(self.mission_text_color, "Final Task: Type the z/OS command to flush the SYSLOG.(D GRS,RESLOG)")
                answer3 = input()
                if answer3.upper() == "D GRS,RESLOG":
                    self.color_print(self.mission_text_color, "Correct! The final encrypted message [G7H8I9] is decrypted to 'SECURE'.")
                    self.color_print(self.mission_text_color, "You've decrypted all messages and saved the mainframe!")

                    # Cancel the timer as the mission is completed
                    t.cancel()

                    self.color_print(self.mission_text_color, "Congratulations, you've completed the game! The mainframe is saved and secure.")
                    self.current_room = "Game_Over"
                    time.sleep(2)
                    self.main_menu()
                else:
                    self.color_print(self.mission_text_color, "Incorrect. You need to complete the mission to move on.")
                    time.sleep(2)
            else:
                self.color_print(self.mission_text_color, "Incorrect. You need to complete the mission to move on.")
                time.sleep(2)
        else:
            self.color_print(self.mission_text_color, "Incorrect. You need to complete the mission to move on.")
            time.sleep(2)

    def main(self):
        self.introduction()
        while True:
            choice = self.menu()
            if choice == '1':
                self.move_to_next_room()
            elif choice == '2':
                self.complete_mission()
            elif choice == '3':
                self.color_print(self.intro_text_color, "Exiting the secret world. Goodbye, Cyber Sleuth!")
                break
            else:
                self.color_print(self.mission_text_color, "Invalid choice. Try again.")


if __name__ == "__main__":
    game = SneakersInspiredRPG()
    game.introduction()
