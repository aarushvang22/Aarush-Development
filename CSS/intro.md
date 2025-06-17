## CSS Basics

```css
selector {
  property: value;
}

p {
  color: blue;
  font-size: 18px;
}
```

---

## Different Use Types of CSS:

### 1. Inline CSS (inside HTML tag):

```html
<p style="color:red;">This is red text.</p>
```

### 2. Internal CSS (in `<style>` tag):

```html
<head>
  <style>
    h1 {
      color: green;
    }
    p {
        color: blue;
    }
  </style>
</head>
```

### 3. External CSS (linked file):

```html
<link rel="stylesheet" href="styles.css">
```

---

## Common Properties

| Property     | Example                    | Description                     |
| ------------ | -------------------------- | ------------------------------- |
| `color`      | `color: blue;`             | Text color                      |
| `background` | `background: yellow;`      | Background color                |
| `font-size`  | `font-size: 16px;`         | Size of the text                |
| `margin`     | `margin: 20px;`            | Space outside the element       |
| `padding`    | `padding: 10px;`           | Space inside the element        |
| `border`     | `border: 1px solid black;` | Adds a border around an element |
