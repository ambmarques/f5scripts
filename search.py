from f5.bigip import ManagementRoot
import sys
import getpass
argument = sys.argv[1]
username = input("Username:")
password = getpass.getpass()

def searchstuff():
	alllbs= [
	"LB IP 1 or LB FQDN 1", 
	"LB IP 2 or LB FQDN 2" 
  ]
	for items in alllbs:
		lb = ManagementRoot(items, username , password)
		virtuals = lb.tm.ltm.virtuals.get_collection()
		poolslb = lb.tm.ltm.pools.get_collection()
		nodes = lb.tm.ltm.nodes.get_collection()
		print(f"\x1b[4;31;40m{items}\x1b[0m")
		for virtual in virtuals:
			address = virtual.destination
			address1 = address.replace("/Common/", "")
			address1 = address1.split(":", 1)
			pool = getattr(virtual,"pool",'')
			pool1 = pool.replace("/Common/", "")
			if address1[0] == argument and hasattr(virtual, "pool") == True:			
				print("Virtual Server -> {}\nPool -> {}\nIP -> {}\nPort -> {}".format(virtual.name, pool1, address1[0], address1[1]))
				for pool in poolslb:
					if pool1 == pool.name:
						print("\x1b[4;37;40mPool Members\x1b[0m")
						for member in pool.members_s.get_collection():
							print("Nodes ->" , member.address, member.state)
							
searchstuff()
