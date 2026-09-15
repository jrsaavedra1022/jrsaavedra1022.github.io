# Dragon Flip — entrega web y preparación de tiendas

## Identidad y URLs

Nombre público: **Dragon Flip**. Se conserva la identidad del proyecto DragonFlip, su dragón esmeralda, alas coral, cuernos marfil y fondo azul profundo. No se ha comprobado disponibilidad comercial del nombre en las tiendas ni marcas registradas.

- Marketing: https://jrsaavedra1022.github.io/apps/dragon-flip/
- Soporte: https://jrsaavedra1022.github.io/apps/dragon-flip/support/
- Privacidad: https://jrsaavedra1022.github.io/apps/dragon-flip/privacy/
- Uso y apoyo al creador: https://jrsaavedra1022.github.io/apps/dragon-flip/terms/
- Inglés: las mismas rutas bajo `/apps/dragon-flip/en/`.

Las tres URLs anteriores bajo `/apps/flappy-dragons/` tienen redirección HTML, enlace manual y canonical al destino nuevo. No son redirecciones HTTP 301: GitHub Pages sirve archivos estáticos. Usar directamente las rutas nuevas en las tiendas. No se altera Popora, SnapClip ni app-ads.txt.

## Fundamento del contenido

Revisado el proyecto local real `DragonFlip`, con referencia adicional a la tarea «Crear prototipo DragonFlip en Godot» y su copia de trabajo. Se revisaron README, scripts, configuración del proyecto y exportación Android.

- `scripts/profile.gd`: guardado local de XP, récord, puntos acumulados, vestuario, idioma, música, efectos y luz estable. `supporter_owned` espera a un futuro proveedor de derechos de compra.
- `scripts/wardrobe.gd`: Espíritu Libre / Free Spirit, 26 cosméticos, compra única opcional, sin ventajas de juego. El propio menú indica que las compras no están disponibles todavía.
- README y lógica: vuelo por impulso, energía, fruta de retroceso, vestidor, 15 mundos y ES/EN.
- No se encontraron HTTPRequest, HTTPClient, WebSocket, ENet, Firebase, analítica, Game Center, StoreKit ni Google Play Billing en scripts/configuración revisados. La exportación Android indica `permissions/internet=false`.
- El propietario confirmó conservar las 26 piezas y ausencia de anuncios. Esto es contenido cosmético opcional, no una propina sin contraprestación ni una donación benéfica.

La privacidad publicada describe la versión actual sin pagos. Es completa para ese alcance e incluye soporte por correo y alojamiento web; no promete que ningún proveedor trate datos. No sustituye la revisión del binario final, plugins, permisos y declaraciones App Privacy/Data safety.

## Antes de habilitar compras

1. Implementar la compra única no consumible del paquete con StoreKit / Google Play Billing, validar derechos y permitir restauración conforme a cada plataforma. El sitio no implementa pagos.
2. Confirmar precio, identificadores del producto, metadatos y alcance exacto. No usar un botón de donación externa para vender el paquete cosmético.
3. Probar compra, cancelación, fallo, reinstalación, restauración y revocación/reembolso en sandbox. No desbloquear compras por un flag local no verificado.
4. Actualizar privacidad con datos de transacción realmente tratados, validación local/servidor, proveedores y conservación. Añadir las prácticas nuevas a App Privacy/Data safety si corresponde.
5. Actualizar las frases «compras aún no disponibles» en ES/EN, tanto marketing como soporte, privacidad y uso. No quitarlas antes de que la integración funcione.
6. Revisar la licencia de la ficha de App Store: la página de uso enlaza al EULA estándar de forma condicional y no constituye una licencia personalizada nueva.
7. Añadir dentro del juego enlaces accesibles de soporte y privacidad. No se modificó el proyecto de Godot en esta tarea.
8. Agregar enlaces reales de descarga y capturas del binario final. La ilustración promocional no debe presentarse como captura de gameplay en las tiendas.

## Imágenes

- `apps/dragon-flip/assets/icon.png`: icono existente del proyecto, reutilizado sin cambiarlo.
- `apps/dragon-flip/assets/hero.png`: ilustración nueva mediante la herramienta integrada de generación de imágenes; 1536 × 1024. Se etiqueta como ilustración promocional, no captura.
- `docs/dragon-flip-image-prompt.txt`: prompt usado para la ilustración. La imagen usa el icono existente como referencia de identidad.
- Tipografía local Lilita One, reutilizada del juego con su licencia OFL en `assets/OFL.txt`.

No se generaron pantallas falsas, enlaces de descarga, reseñas, precios ni cifras de usuarios.

## Referencias

- https://developer.apple.com/app-store/review/guidelines/ (compras dentro de la app, contenido cosmético y exactitud del marketing)
- https://support.google.com/googleplay/android-developer/answer/9858738 (contenido digital y pagos)
- https://www.apple.com/legal/internet-services/itunes/dev/stdeula/
- https://support.apple.com/en-us/118223
- https://support.google.com/googleplay/answer/2479637
- https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement
