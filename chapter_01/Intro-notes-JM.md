# Hash Tables

Data structure mapping keys to values for effitient lookup.
Common simple implementation:
1. Compute the key's hash code (int or long).
2. Map the hash code to an index in the array, e.g. with `hash(key) % array_length`
3. 