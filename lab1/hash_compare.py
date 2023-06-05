#!python3
#import binascii
import subprocess
import argparse


def hash_file(filename):
	cmd = f'openssl dgst -md5 -hmac "abcdefg" {filename}'
	output = subprocess.run(cmd.split(' '), capture_output=True)
	str_hash = str(output.stdout.strip()).split(' ')[-1][:-1]
	int_hash = int(str_hash, 16)
	return int_hash


def compare_hash_bits(a_hash, b_hash, verbose=False):
	# Choosing to disallow hashes of different lengths
	assert(len(str(a_hash)) == len(str(b_hash)))
	diff = 0
	n = len(str(a_hash))*8
	for i in range(n):
		a_bit = (a_hash >> i) & 1
		b_bit = (b_hash >> i) & 1
		if verbose:
			print('{0} {1} {2}'.format(a_bit, ' ' if a_bit == b_bit else '*', b_bit))
		diff += int(a_bit != b_bit)
	print(f'Same: {n-diff}')
	print(f'Diff: {diff}')
			

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('a', help='first file to compare hash of')
	parser.add_argument('b', help='second file to compare hash of')
	args = parser.parse_args()
	
	a_hash = hash_file(args.a)
	b_hash = hash_file(args.b)

	print(f'a_hash: {a_hash}')
	print(f'b_hash: {b_hash}')
	
	compare_hash_bits(a_hash, b_hash, verbose=True)


if __name__ == '__main__':
	main()
