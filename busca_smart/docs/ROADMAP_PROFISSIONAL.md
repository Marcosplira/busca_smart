# 🚀 Roadmap Profissional de Desenvolvimento — BuscaSmart
## Do MVP Funcional à Publicação na Google Play Store e Expansão Tecnológica

---

## 📅 Visão Geral do Cronograma

```
[FASE 1: MVP Web & GIS] ──► [FASE 2: Teste de Campo Picuí] ──► [FASE 3: Android APK & Play Store]
       (CONCLUÍDA)                   (Q1 2027)                             (Q2 2027)
                                                                               │
[FASE 6: Drones Térmicos] ◄── [FASE 5: Rádio Mesh LoRa] ◄── [FASE 4: Mapas Vetoriais MBTiles]
       (Q4 2027)                     (Q3 2027)                             (Q3 2027)
```

---

## 🎯 Detalhamento das Fases

### ✅ Fase 1: MVP 1.0 Web & Mobile Responsive (CONCLUÍDA)
- [x] Arquitetura Django 5 com autenticação e níveis de acesso (Coordenador vs Voluntário).
- [x] Integração de camadas de satélite de alta definição (Esri World Imagery).
- [x] Ferramenta de desenho vetorial (Leaflet Draw) com medição de área em hectares e km².
- [x] Motor de partição matemática de setores via `Turf.js`.
- [x] Módulo de equipe com código de convite rápido e QR Code dinâmico.
- [x] Tela mobile de telemetria GPS e modo offline em HTML5.
- [x] Resumo tático situacional com IA e Chatbot conversacional com respostas SAR especializadas.
- [x] Geração de Relatório Oficial de Missão SAR pronto para impressão A4 e PDF.
- [x] Central de documentação executiva e apresentação em slides (`docs/`).

---

### ⏳ Fase 2: Simulação de Campo e Validação com Forças de Resgate (Q1 2027)
- **Local:** Região rural de Picuí - PB e serra adjacente.
- **Objetivos:**
  - Testar a precisão do GPS dos voluntários sob cobertura vegetal densa.
  - Medir o consumo de bateria de smartphones comuns durante 4 horas contínuas de varredura.
  - Colher feedback de usabilidade de voluntários reais (legibilidade ao sol forte, tamanho de botões).
  - Ajustar o algoritmo de partição para considerar curvas de nível e estradas de terra.

---

### ⏳ Fase 3: Empacotamento Nativo Android & Publicação na Play Store (Q2 2027)
- **Tecnologia:** Capacitor 6 + Android Studio.
- **Entregáveis:**
  - Compilação do arquivo executável de teste (`BuscaSmart-v1.0.apk`).
  - Geração do pacote assinado para distribuição (`BuscaSmart.aab`).
  - Criação da conta de desenvolvedor na Google Play Console.
  - Conformidade com as políticas da Google Play Store (Target SDK 34/35, política de privacidade LGPD, permissão de localização em primeiro plano).
  - Publicação oficial aberta para download por voluntários em todo o Brasil.

---

### 🔮 Fase 4: Mapas Vetoriais MBTiles Offline (Q3 2027)
- **Objetivo:** Permitir o download de mapas de regiões inteiras (ex: todo o município de Picuí - PB) em pacotes compactados de 50 MB no celular.
- **Tecnologia:** MapLibre GL JS + Tilesets OpenMapTiles em formato SQLite `.mbtiles`.

---

### 🔮 Fase 5: Integração com Redes Mesh LoRa (Comunicação Sem Celular) (Q3 2027)
- **Objetivo:** Comunicação e rastreamento de voluntários mesmo sem chip de operadora e sem internet.
- **Tecnologia:** Módulos de rádio de longo alcance LoRa (ex: Meshtastic 915 MHz).
- **Funcionamento:** Cada aparelho de celular conecta via Bluetooth ao rádio no bolso do voluntário. Os rádios formam uma rede repetidora automática cobrindo até 15 km de raio na serra.

---

### 🔮 Fase 6: Integração de Drones SAR e Termografia (Q4 2027)
- **Objetivo:** Carregar ortofotos térmicas geradas por drones na mesma tela do satélite.
- **Tecnologia:** Web-GIS com suporte a camadas GeoTIFF e sensores de calor para busca noturna.
