# Personal Data 🦆

```
    __
   /  \
  /    \___
 /   /\    \
/___/  \____\
   \__/
    ||
   <  >
    ||
   /__\
```

This project focuses on protecting and handling Personally Identifiable Information (PII) securely.

```
  _      _      _
>(.)__ >(.)__ >(.)__
 (___/  (___/  (___/
```

## Learning Objectives

- Examples of Personally Identifiable Information (PII)
- How to implement a log filter that will obfuscate PII fields
- How to encrypt a password and check the validity of an input password
- How to authenticate to a database using environment variables

## Requirements

```
      __     __     __
   __(  )___(  )___(  )___
  (___)(___)(___)(___)(___)
    Duck squad checking requirements!
```

- All files interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.9)
- All files should end with a new line
- First line of all files should be `#!/usr/bin/env python3`
- Code should use pycodestyle style (version 2.5)
- All files must be executable
- All modules, classes, and functions must have documentation
- All functions should be type annotated

```
   __
  /  \___    "Quack quack! Good code!"
 | ^  ^ |
  \ oo /
   \__/
```

## Tasks

```
    __
   /  \    Duck says: "Let's secure that data!"
  / ^^ \
 /  /\  \
/__/  \__\
```

### 0. Regex-ing 🦆
Implement `filter_datum` function to obfuscate PII fields in log messages.

### 1. Log formatter 🦆
Implement `RedactingFormatter` class to filter values in log records.

### 2. Create logger 🦆
Implement `get_logger` function and define `PII_FIELDS` constant.

### 3. Connect to secure database 🦆
Implement `get_db` function to connect to MySQL database using environment variables.

### 4. Read and filter data 🦆
Implement `main` function to retrieve and display filtered user data.

### 5. Encrypting passwords 🦆
Implement `hash_password` function using bcrypt.

### 6. Check valid password 🦆
Implement `is_valid` function to validate passwords against hashed versions.

```
    ___
  <(o )___
   ( ._> /
    `---'
  Security Duck approves this code!
```
