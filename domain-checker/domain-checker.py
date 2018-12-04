from __future__ import print_function

import subprocess

keywords = {"Domain Name": "name",
			"Registry Domain ID": "domain_id",
			"Registrar WHOIS Server": "whois_server",
			"Registrar URL": "registrar_url",
			"Updated Date": "last_update",
			"Creation Date": "create_date",
			"Registry Expiry Date": "exp_date",
			"Registrar": "registrar_name",
			"Registrant Organization": "owner_org",
			"Registrant State/Province": "owner_state",
			"Registrant Country": "owner_country",
			"Registrant Email": "owner_email"}


class Domain(object):

	def __init__(self, name):
		self.name = name
		self.exp_date = None
		self.domain_id = None
		self.available = None
		self.owner_org = None
		self.last_update = None
		self.create_date = None
		self.owner_state = None
		self.owner_email = None
		self.whois_server = None
		self.owner_country = None
		self.registrar_url = None
		self.registrar_name = None

		self.init_params()

	def init_params(self):
		p = subprocess.Popen(['whois', '-H', self.name],
							stdout=subprocess.PIPE,
							stderr=subprocess.PIPE)

		out = p.communicate()[0].split('\n')
		for line in out:
			res = self.__parse_info(line)
			if res:
				setattr(self, res[0], res[1])

		if self.available is None:
			self.available = False

	def __parse_info(self, line):
		if "No match for domain" in line:
			return ("available", True)
		for key in keywords:
			if key+":" in line:
				attr = keywords[key]
				val = line.split(key+":")[1].strip()
				return (attr, val)

		return None	

	def stringify(self):
		res = str()
		for key in keywords:
			attr = getattr(self, keywords[key], '')
			if attr:
				res += key + ": " + attr + '\n'
		if self.available:
			res += 'Available: YES'
			
		return res


def whois(domain_name):
	domain = Domain(domain_name)
	return domain
