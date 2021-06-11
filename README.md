## Masonite sandbox

### Setup

```
$ cd masonite_sandbox/
$ pipenv install -r requirements.txt
$ pipenv run craft install
```

generate key

```
$ pipenv run craft key
```

edit .env

```
DB_CONNECTION=sqlite
```


```
$ pipenv run craft migrate
```

```
$ npm install && npm run dev
```

### run

```
$ pipenv run craft serve
```