import streamlit as st
import requests

# ==========================================
# CONEXIÓN SHEETDB (GOOGLE DRIVE)
# ==========================================
API_URL = "https://sheetdb.io/api/v1/uty19fdz5dh6r"

st.set_page_config(
    page_title="Pesca Baradero — Control de Salida",
    page_icon="🎣",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==========================================
# ESTILOS FINTECH / CLEAN MODERN UI (+60 AÑOS)
# ==========================================
st.markdown("""
<style>
    /* Fondo general y tipografía de alto contraste */
    .stApp {
        background-color: #f8fafc;
        color: #0f172a;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    }
    
    #MainMenu, footer, header[data-testid="stHeader"] {
        visibility: hidden;
        height: 0;
    }
    .block-container {
        padding-top: 1.5rem !important;
        padding-bottom: 3rem !important;
        max-width: 1200px !important;
    }

    /* Pestañas estilo píldora redondeada */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px !important;
        background-color: transparent !important;
        padding-bottom: 12px !important;
        border-bottom: none !important;
    }
    .stTabs [data-baseweb="tab-highlight"],
    .stTabs [data-baseweb="tab-border"] {
        display: none !important;
        visibility: hidden !important;
    }
    .stTabs button[data-baseweb="tab"] {
        background-color: #ffffff !important;
        color: #475569 !important;
        border: 1.5px solid #cbd5e1 !important;
        border-radius: 9999px !important;
        padding: 8px 22px !important;
        font-size: 1.05rem !important;
        font-weight: 700 !important;
        box-shadow: 0 1px 3px rgba(0,0,0,0.03) !important;
        transition: all 0.15s ease !important;
    }
    .stTabs button[data-baseweb="tab"]:hover {
        border-color: #0284c7 !important;
        color: #0284c7 !important;
        background-color: #f0f9ff !important;
    }
    .stTabs button[data-baseweb="tab"][aria-selected="true"] {
        background-color: #0284c7 !important;
        color: #ffffff !important;
        border: 1.5px solid #0284c7 !important;
        box-shadow: 0 4px 12px rgba(2, 132, 199, 0.25) !important;
    }

    /* Tarjetas nativas de trabajo */
    div[data-testid="stVerticalBlockBorderWrapper"] > div {
        background-color: #ffffff !important;
        border: 1.5px solid #e2e8f0 !important;
        border-radius: 20px !important;
        padding: 24px 28px !important;
        box-shadow: 0 4px 16px rgba(15, 23, 42, 0.04) !important;
        margin-bottom: 20px !important;
    }

    /* Alineación vertical perfecta de filas de ítems */
    div[data-testid="stHorizontalBlock"] {
        align-items: center !important;
    }

    /* Controles de formulario grandes y legibles */
    input[type="text"], input[type="number"], .stSelectbox div[data-baseweb="select"] {
        font-size: 1.1rem !important;
        font-weight: 600 !important;
        color: #0f172a !important;
        background-color: #f8fafc !important;
        border: 1.5px solid #cbd5e1 !important;
        border-radius: 12px !important;
        min-height: 2.7rem !important;
    }
    input:focus {
        border-color: #0284c7 !important;
        background-color: #ffffff !important;
    }
    div[data-testid="stCheckbox"] label span {
        font-size: 1.25rem !important;
        font-weight: 700 !important;
        color: #0f172a !important;
    }

    /* Indicador de carga estilizado tipo píldora flotante */
    div[data-testid="stSpinner"] {
        background: #ffffff !important;
        border: 1.5px solid #0284c7 !important;
        border-radius: 9999px !important;
        padding: 12px 24px !important;
        box-shadow: 0 4px 16px rgba(2, 132, 199, 0.15) !important;
        color: #0284c7 !important;
        font-weight: 700 !important;
        font-size: 1.05rem !important;
        margin: 12px 0 !important;
    }

    /* Insignia de total gastado */
    .badge-gasto-total {
        background-color: #ecfdf5;
        color: #065f46;
        border: 1.5px solid #a7f3d0;
        font-size: 1.15rem;
        font-weight: 800;
        padding: 6px 18px;
        border-radius: 9999px;
        display: inline-flex;
        align-items: center;
    }

    /* Botones principales de acción */
    div.stButton > button, div.stFormSubmitButton > button {
        border-radius: 9999px !important;
        font-weight: 800 !important;
        font-size: 1.05rem !important;
        min-height: 3.1rem !important;
        transition: all 0.2s ease !important;
    }
    div.stButton > button:first-child {
        background: linear-gradient(135deg, #0284c7 0%, #0369a1 100%) !important;
        color: #ffffff !important;
        border: none !important;
        box-shadow: 0 4px 14px rgba(2, 132, 199, 0.25) !important;
    }

    /* Popovers limpios con texto oscuro asegurado */
    div[data-testid="stPopover"] > button {
        background-color: #ffffff !important;
        color: #0369a1 !important;
        border: 1.5px solid #bae6fd !important;
        border-radius: 9999px !important;
        min-height: 2.6rem !important;
        padding: 4px 18px !important;
        font-weight: 800 !important;
    }
    div[data-testid="stPopover"] > button p,
    div[data-testid="stPopover"] > button span {
        color: #0369a1 !important;
        font-weight: 800 !important;
    }
    div[data-testid="stPopoverBody"] {
        background-color: #ffffff !important;
        border: 1.5px solid #cbd5e1 !important;
        border-radius: 18px !important;
        padding: 20px !important;
        box-shadow: 0 12px 30px rgba(15, 23, 42, 0.12) !important;
    }
    div[data-testid="stPopoverBody"] p,
    div[data-testid="stPopoverBody"] span,
    div[data-testid="stPopoverBody"] label {
        color: #0f172a !important;
    }

    /* Chips de estado en Cuentas Claras */
    .fintech-chip {
        padding: 6px 16px;
        border-radius: 9999px;
        font-weight: 800;
        font-size: 0.95rem;
        display: inline-flex;
        align-items: center;
    }
    .chip-green {
        background-color: #ecfdf5;
        color: #065f46;
        border: 1px solid #a7f3d0;
    }
    .chip-red {
        background-color: #fef2f2;
        color: #991b1b;
        border: 1px solid #fecaca;
    }
    .chip-gray {
        background-color: #f1f5f9;
        color: #475569;
        border: 1px solid #e2e8f0;
    }
</style>
""", unsafe_allow_html=True)

# Encabezado principal
st.markdown("""
<div style="background: #ffffff; border: 1.5px solid #e2e8f0; border-radius: 20px; padding: 20px 26px; margin-bottom: 16px; box-shadow: 0 2px 8px rgba(15, 23, 42, 0.03);">
    <div style="font-size: 2rem; font-weight: 900; color: #0284c7; letter-spacing: -0.5px;">🎣 Pesca Baradero</div>
    <div style="color: #64748b; font-size: 1rem; font-weight: 500; margin-top: 2px;">Logística de víveres, compras y división de gastos</div>
</div>
""", unsafe_allow_html=True)

# ==========================================
# SISTEMA DE NOTIFICACIONES PERSISTENTES
# ==========================================
def notificar(mensaje, tipo="success"):
    st.session_state["flash_mensaje"] = mensaje
    st.session_state["flash_tipo"] = tipo

if "flash_mensaje" in st.session_state:
    f_tipo = st.session_state.pop("flash_tipo", "success")
    f_msg = st.session_state.pop("flash_mensaje")
    if f_tipo == "success":
        st.success(f_msg, icon="✅")
        st.toast(f_msg, icon="✅")
    elif f_tipo == "info":
        st.info(f_msg, icon="ℹ️")
        st.toast(f_msg, icon="ℹ️")
    elif f_tipo == "warning":
        st.warning(f_msg, icon="⚠️")
        st.toast(f_msg, icon="⚠️")

# ==========================================
# FUNCIONES SHEETDB (GOOGLE DRIVE)
# ==========================================
def cargar_tareas_drive():
    try:
        r = requests.get(f"{API_URL}?sheet=Tareas", timeout=7)
        return r.json()
    except Exception:
        return []

def cargar_pescadores_drive():
    try:
        r = requests.get(f"{API_URL}?sheet=Gastos", timeout=7).json()
        amigos = [str(x.get("amigo")).strip().title() for x in r if x.get("amigo")]
        if amigos:
            return amigos
    except Exception:
        pass
    return ["Alan", "Dylan", "Michel", "Sebastian"]

def sincronizar_pestana_gastos_drive(todas_las_tareas, lista_pescadores):
    totales = {p: 0.0 for p in lista_pescadores}
    for t in todas_las_tareas:
        resp = t.get("responsable", "").strip().title()
        if resp in totales:
            try:
                totales[resp] += float(t.get("Gastos") or t.get("gastos") or 0.0)
            except (ValueError, TypeError):
                pass
    for amigo, total in totales.items():
        try:
            requests.patch(f"{API_URL}/amigo/{amigo}?sheet=Gastos", json={"monto": str(total)}, timeout=4)
        except Exception:
            pass

def agregar_pescador_drive(nombre):
    payload = {"data": [{"amigo": nombre.strip().title(), "monto": "0"}]}
    try:
        requests.post(f"{API_URL}?sheet=Gastos", json=payload, timeout=6)
    except Exception:
        pass

def reemplazar_pescador_drive(nombre_viejo, nombre_nuevo):
    n_viejo = nombre_viejo.strip().title()
    n_nuevo = nombre_nuevo.strip().title()
    try:
        requests.patch(f"{API_URL}/amigo/{n_viejo}?sheet=Gastos", json={"amigo": n_nuevo}, timeout=6)
    except Exception:
        pass
    try:
        requests.patch(f"{API_URL}/responsable/{n_viejo}?sheet=Tareas", json={"responsable": n_nuevo}, timeout=6)
    except Exception:
        pass

def borrar_pescador_drive(nombre):
    try:
        requests.delete(f"{API_URL}/amigo/{nombre}?sheet=Gastos", timeout=6)
    except Exception:
        pass

def actualizar_fila_drive(row_id, resp, item, estado_comprado, monto_gasto):
    val_estado = "1" if estado_comprado else "0"
    payload = {
        "responsable": str(resp).strip(),
        "item": str(item).strip(),
        "estado": val_estado,
        "Gastos": str(monto_gasto)
    }
    try:
        requests.patch(f"{API_URL}/id/{row_id}?sheet=Tareas", json=payload, timeout=6)
    except Exception:
        pass

def agregar_fila_drive(nueva_id, resp, item, monto):
    payload = {
        "data": [{
            "id": str(nueva_id),
            "responsable": str(resp).strip(),
            "item": str(item).strip(),
            "estado": "0",
            "Gastos": str(monto)
        }]
    }
    try:
        requests.post(f"{API_URL}?sheet=Tareas", json=payload, timeout=6)
    except Exception:
        pass

def borrar_fila_drive(row_id):
    try:
        requests.delete(f"{API_URL}/id/{row_id}?sheet=Tareas", timeout=6)
    except Exception:
        pass

def reiniciar_salida_drive(tareas, pescadores):
    for t in tareas:
        t_id = t.get("id")
        try:
            requests.patch(f"{API_URL}/id/{t_id}?sheet=Tareas", json={"estado": "0", "Gastos": "0"}, timeout=3)
        except Exception:
            pass
    for p in pescadores:
        try:
            requests.patch(f"{API_URL}/amigo/{p}?sheet=Gastos", json={"monto": "0"}, timeout=3)
        except Exception:
            pass

# ==========================================
# CARGA BAJO DEMANDA (OPTIMIZACIÓN DE MEMORIA)
# ==========================================
if "todas_tareas" not in st.session_state or "amigos_pescadores" not in st.session_state:
    st.session_state["todas_tareas"] = cargar_tareas_drive()
    st.session_state["amigos_pescadores"] = cargar_pescadores_drive()

todas_tareas = st.session_state["todas_tareas"]
amigos_pescadores = st.session_state["amigos_pescadores"]

max_id = 0
for t in todas_tareas:
    try:
        max_id = max(max_id, int(t.get("id", 0)))
    except (ValueError, TypeError):
        pass

tareas_compras = [t for t in todas_tareas if t.get("responsable", "").strip().lower() != "recordatorio"]
tareas_recordatorios = [t for t in todas_tareas if t.get("responsable", "").strip().lower() == "recordatorio"]

lugares_detectados = []
for t in tareas_compras:
    r = t.get("responsable", "").strip()
    if r.title() not in amigos_pescadores and r not in lugares_detectados and r:
        lugares_detectados.append(r)

if not lugares_detectados:
    lugares_detectados = ["Despensa Baradero"]

# Pestañas principales
tab_compras, tab_cuentas, tab_recordatorios, tab_ajustes = st.tabs([
    "🛒 Compras & Tareas",
    "💰 Cuentas Claras",
    "🎒 Recordatorios",
    "⚙️ Pescadores & Lugares"
])

# ------------------------------------------------------------------------------
# PESTAÑA 1: COMPRAS POR INTEGRANTE / LUGAR
# ------------------------------------------------------------------------------
with tab_compras:
    col_info, col_refresh = st.columns([3.8, 1.2])
    with col_info:
        st.markdown("""
        <div style="background-color: #f1f5f9; border: 1.5px solid #e2e8f0; border-radius: 9999px; padding: 10px 22px; font-weight: 600; color: #334155; font-size: 1rem;">
            💡 Editá nombres o gastos y tocá <b>Guardar cambios</b> al pie de la solapa.
        </div>
        """, unsafe_allow_html=True)
    with col_refresh:
        if st.button("🔄 Refrescar desde Drive", key="btn_act_compras", use_container_width=True):
            with st.spinner("Conectando con Google Drive... por favor espere..."):
                st.session_state["todas_tareas"] = cargar_tareas_drive()
                st.session_state["amigos_pescadores"] = cargar_pescadores_drive()
                notificar("Datos actualizados desde Google Drive.")
                st.rerun()

    st.write("")

    if not todas_tareas:
        st.warning("Cargando lista desde Google Drive o revisá la conexión...")
    else:
        etiquetas_subtabs = [f"🏪 {lugar}" for lugar in lugares_detectados] + [f"👤 {amigo}" for amigo in amigos_pescadores]
        subtabs = st.tabs(etiquetas_subtabs)

        # 1. SOLAPAS DE LUGARES EXTERNOS
        for i_lug, lugar in enumerate(lugares_detectados):
            with subtabs[i_lug]:
                items_lugar = [t for t in tareas_compras if t.get("responsable", "").strip().lower() == lugar.lower()]

                with st.container(border=True):
                    col_l1, col_l2 = st.columns([3, 1.3])
                    with col_l1:
                        st.markdown(f"<div style='font-size: 1.6rem; font-weight: 900; color: #0284c7;'>🏪 {lugar}</div>", unsafe_allow_html=True)
                        st.caption("Compras generales a realizar en este punto de parada.")
                    with col_l2:
                        with st.popover("✏️ Cambiar nombre", use_container_width=True):
                            st.markdown("<p style='font-weight:bold; color:#0f172a; margin-bottom:4px;'>Editar nombre del lugar:</p>", unsafe_allow_html=True)
                            nuevo_nombre_lugar = st.text_input("Nombre:", value=lugar, key=f"renom_{lugar}", label_visibility="collapsed")
                            if st.button("Aplicar cambio", key=f"btn_renom_{lugar}", use_container_width=True):
                                if nuevo_nombre_lugar.strip() and nuevo_nombre_lugar.strip() != lugar:
                                    n_lug_clean = nuevo_nombre_lugar.strip()
                                    with st.spinner(f"Renombrando a '{n_lug_clean}' en Google Drive..."):
                                        for it in items_lugar:
                                            actualizar_fila_drive(it.get("id"), n_lug_clean, it.get("item"), str(it.get("estado")) == "1", it.get("Gastos", 0))
                                        st.session_state["todas_tareas"] = cargar_tareas_drive()
                                        notificar(f"Se renombró el lugar a '{n_lug_clean}' correctamente.")
                                        st.rerun()

                    st.write("")

                    if items_lugar:
                        h1, h2, h3, h4, h5 = st.columns([0.6, 3.2, 2.2, 1.8, 0.8])
                        with h1: st.markdown("<div style='color:#64748b; font-weight:800; font-size:0.85rem; text-transform:uppercase;'>Listo</div>", unsafe_allow_html=True)
                        with h2: st.markdown("<div style='color:#64748b; font-weight:800; font-size:0.85rem; text-transform:uppercase;'>Artículo</div>", unsafe_allow_html=True)
                        with h3: st.markdown("<div style='color:#64748b; font-weight:800; font-size:0.85rem; text-transform:uppercase;'>Quién lo paga</div>", unsafe_allow_html=True)
                        with h4: st.markdown("<div style='color:#64748b; font-weight:800; font-size:0.85rem; text-transform:uppercase;'>Gasto ($)</div>", unsafe_allow_html=True)
                        with h5: st.markdown("<div style='color:#64748b; font-weight:800; font-size:0.85rem; text-transform:uppercase;'>Borrar</div>", unsafe_allow_html=True)

                    cambios_lugar = []
                    for it in items_lugar:
                        it_id = it.get("id")
                        orig_item = str(it.get("item", ""))
                        orig_chk = str(it.get("estado", "0")) == "1"
                        try:
                            orig_gasto = float(it.get("Gastos") or it.get("gastos") or 0.0)
                        except (ValueError, TypeError):
                            orig_gasto = 0.0

                        c1, c2, c3, c4, c5 = st.columns([0.6, 3.2, 2.2, 1.8, 0.8])
                        with c1:
                            chk_val = st.checkbox("", value=orig_chk, key=f"l_chk_{it_id}", label_visibility="collapsed")
                        with c2:
                            txt_val = st.text_input("Artículo", value=orig_item, key=f"l_txt_{it_id}", label_visibility="collapsed")
                        with c3:
                            opciones_pagador = ["— Sin pagar —"] + amigos_pescadores
                            pagador_sel = st.selectbox("Quién lo paga", opciones_pagador, index=0, key=f"l_paga_{it_id}", label_visibility="collapsed")
                        with c4:
                            num_val = st.number_input("Gasto $", value=orig_gasto, min_value=0.0, step=500.0, format="%.2f", key=f"l_num_{it_id}", label_visibility="collapsed")
                        with c5:
                            with st.popover("🗑️", help="Eliminar ítem"):
                                st.markdown(f"**¿Deseas eliminar '{orig_item}'?**")
                                st.caption("Esta acción quitará el ítem de la lista y de tu Google Sheet.")
                                col_si, col_no = st.columns(2)
                                with col_si:
                                    if st.button("Sí", key=f"del_si_l_{it_id}", type="primary", use_container_width=True):
                                        with st.spinner(f"Eliminando '{orig_item}' de Google Drive..."):
                                            borrar_fila_drive(it_id)
                                            st.session_state["todas_tareas"] = [t for t in st.session_state["todas_tareas"] if str(t.get("id")) != str(it_id)]
                                            sincronizar_pestana_gastos_drive(st.session_state["todas_tareas"], st.session_state["amigos_pescadores"])
                                            notificar(f"Se eliminó '{orig_item}' correctamente.")
                                            st.rerun()
                                with col_no:
                                    if st.button("No", key=f"del_no_l_{it_id}", use_container_width=True):
                                        st.rerun()

                        cambios_lugar.append({
                            "id": it_id, "item": txt_val, "chk": chk_val, "gasto": num_val,
                            "pagador": pagador_sel, "orig_item": orig_item, "orig_chk": orig_chk,
                            "orig_gasto": orig_gasto
                        })

                    st.write("")
                    if st.button(f"💾 Guardar cambios de {lugar}", key=f"btn_save_lug_{lugar}", use_container_width=True):
                        with st.spinner(f"Guardando cambios de {lugar} en Google Drive..."):
                            hubo_cambios = False
                            for row in cambios_lugar:
                                f_id = row["id"]
                                nuevo_resp = row["pagador"] if row["pagador"] != "— Sin pagar —" else lugar
                                if (row["item"].strip() != row["orig_item"].strip() or
                                    row["chk"] != row["orig_chk"] or
                                    abs(row["gasto"] - row["orig_gasto"]) > 0.01 or
                                    row["pagador"] != "— Sin pagar —"):
                                    actualizar_fila_drive(f_id, nuevo_resp, row["item"], row["chk"], row["gasto"])
                                    for t in st.session_state["todas_tareas"]:
                                        if str(t.get("id")) == str(f_id):
                                            t["responsable"] = nuevo_resp
                                            t["item"] = row["item"].strip()
                                            t["estado"] = "1" if row["chk"] else "0"
                                            t["Gastos"] = str(row["gasto"])
                                    hubo_cambios = True
                            sincronizar_pestana_gastos_drive(st.session_state["todas_tareas"], st.session_state["amigos_pescadores"])
                            if hubo_cambios:
                                notificar(f"Se guardaron los cambios de {lugar} correctamente.")
                            else:
                                notificar(f"No hubo cambios pendientes para guardar en {lugar}.", tipo="info")
                            st.rerun()

                    with st.expander(f"➕ Sumar ítem a {lugar}"):
                        c_n, c_p = st.columns([3, 2])
                        with c_n: in_art = st.text_input("Qué comprar:", placeholder="Ej: Hielo, carbón...", key=f"in_art_{lugar}")
                        with c_p: in_cos = st.number_input("Costo estimado ($):", min_value=0.0, step=500.0, format="%.2f", key=f"in_cos_{lugar}")
                        if st.button(f"➕ Agregar a {lugar}", key=f"btn_add_item_{lugar}", use_container_width=True):
                            if in_art.strip():
                                with st.spinner(f"Agregando '{in_art.strip()}' a Google Drive..."):
                                    agregar_fila_drive(max_id + 1, lugar, in_art.strip(), in_cos)
                                    st.session_state["todas_tareas"].append({
                                        "id": str(max_id + 1), "responsable": lugar, "item": in_art.strip(), "estado": "0", "Gastos": str(in_cos)
                                    })
                                    sincronizar_pestana_gastos_drive(st.session_state["todas_tareas"], st.session_state["amigos_pescadores"])
                                    notificar(f"Se agregó '{in_art.strip()}' a {lugar} correctamente.")
                                    st.rerun()

        # 2. SOLAPAS INDIVIDUALES DE PESCADORES
        offset_lugares = len(lugares_detectados)
        for i_amigo, amigo in enumerate(amigos_pescadores):
            with subtabs[offset_lugares + i_amigo]:
                items_amigo = [t for t in tareas_compras if t.get("responsable", "").strip().lower() == amigo.lower()]
                total_gastado = sum([float(it.get("Gastos") or it.get("gastos") or 0.0) for it in items_amigo])

                with st.container(border=True):
                    col_t, col_b = st.columns([2.8, 1.5])
                    with col_t:
                        st.markdown(f"<div style='font-size: 1.6rem; font-weight: 900; color: #059669;'>👤 {amigo}</div>", unsafe_allow_html=True)
                        st.caption("Compras y tareas asignadas a este pescador.")
                    with col_b:
                        with st.popover("✏️ Reemplazar pescador", use_container_width=True):
                            st.markdown("<p style='font-weight:bold; color:#0f172a; margin-bottom:4px;'>Editar o reemplazar pescador:</p>", unsafe_allow_html=True)
                            st.caption(f"Si {amigo} no viaja y va otra persona, ingresá el nuevo nombre.")
                            nuevo_nombre_amigo = st.text_input("Nombre nuevo:", value=amigo, key=f"renom_p_{amigo}")
                            if st.button("Guardar reemplazo", key=f"btn_renom_p_{amigo}", use_container_width=True):
                                if nuevo_nombre_amigo.strip() and nuevo_nombre_amigo.strip().title() != amigo:
                                    n_clean = nuevo_nombre_amigo.strip().title()
                                    with st.spinner(f"Reemplazando a {amigo} por {n_clean} en Drive..."):
                                        reemplazar_pescador_drive(amigo, n_clean)
                                        st.session_state["amigos_pescadores"] = [n_clean if x == amigo else x for x in st.session_state["amigos_pescadores"]]
                                        for t in st.session_state["todas_tareas"]:
                                            if t.get("responsable", "").strip().lower() == amigo.lower():
                                                t["responsable"] = n_clean
                                        sincronizar_pestana_gastos_drive(st.session_state["todas_tareas"], st.session_state["amigos_pescadores"])
                                        notificar(f"Se reemplazó a {amigo} por {n_clean} con éxito.")
                                        st.rerun()

                        st.markdown(f"<div style='margin-top: 10px; text-align: right;'><span class='badge-gasto-total'>Total aportado: ${total_gastado:,.2f}</span></div>", unsafe_allow_html=True)

                    st.write("")

                    if items_amigo:
                        h1, h2, h3, h4 = st.columns([0.6, 3.4, 2.0, 0.8])
                        with h1: st.markdown("<div style='color:#64748b; font-weight:800; font-size:0.85rem; text-transform:uppercase;'>Listo</div>", unsafe_allow_html=True)
                        with h2: st.markdown("<div style='color:#64748b; font-weight:800; font-size:0.85rem; text-transform:uppercase;'>Artículo</div>", unsafe_allow_html=True)
                        with h3: st.markdown("<div style='color:#64748b; font-weight:800; font-size:0.85rem; text-transform:uppercase;'>Gasto ($)</div>", unsafe_allow_html=True)
                        with h4: st.markdown("<div style='color:#64748b; font-weight:800; font-size:0.85rem; text-transform:uppercase;'>Borrar</div>", unsafe_allow_html=True)

                    cambios_p = []
                    for it in items_amigo:
                        it_id = it.get("id")
                        orig_item = str(it.get("item", ""))
                        orig_chk = str(it.get("estado", "0")) == "1"
                        try:
                            orig_gasto = float(it.get("Gastos") or it.get("gastos") or 0.0)
                        except (ValueError, TypeError):
                            orig_gasto = 0.0

                        c1, c2, c3, c4 = st.columns([0.6, 3.4, 2.0, 0.8])
                        with c1:
                            chk_val = st.checkbox("", value=orig_chk, key=f"p_chk_{it_id}", label_visibility="collapsed")
                        with c2:
                            txt_val = st.text_input("Artículo", value=orig_item, key=f"p_txt_{it_id}", label_visibility="collapsed")
                        with c3:
                            num_val = st.number_input("Gasto $", value=orig_gasto, min_value=0.0, step=500.0, format="%.2f", key=f"p_num_{it_id}", label_visibility="collapsed")
                        with c4:
                            with st.popover("🗑️", help="Eliminar ítem"):
                                st.markdown(f"**¿Deseas eliminar '{orig_item}'?**")
                                st.caption("Se quitará de la lista y de tu Google Sheet.")
                                col_si, col_no = st.columns(2)
                                with col_si:
                                    if st.button("Sí", key=f"del_si_p_{it_id}", type="primary", use_container_width=True):
                                        with st.spinner(f"Eliminando '{orig_item}' de Google Drive..."):
                                            borrar_fila_drive(it_id)
                                            st.session_state["todas_tareas"] = [t for t in st.session_state["todas_tareas"] if str(t.get("id")) != str(it_id)]
                                            sincronizar_pestana_gastos_drive(st.session_state["todas_tareas"], st.session_state["amigos_pescadores"])
                                            notificar(f"Se eliminó '{orig_item}' correctamente.")
                                            st.rerun()
                                with col_no:
                                    if st.button("No", key=f"del_no_p_{it_id}", use_container_width=True):
                                        st.rerun()

                        cambios_p.append({
                            "id": it_id, "item": txt_val, "chk": chk_val, "gasto": num_val,
                            "orig_item": orig_item, "orig_chk": orig_chk, "orig_gasto": orig_gasto
                        })

                    st.write("")
                    if st.button(f"💾 Guardar cambios de {amigo}", key=f"btn_save_bottom_{amigo}", use_container_width=True):
                        with st.spinner(f"Guardando cambios de {amigo} en Google Drive..."):
                            hubo_cambios = False
                            for row in cambios_p:
                                f_id = row["id"]
                                if (row["item"].strip() != row["orig_item"].strip() or
                                    row["chk"] != row["orig_chk"] or
                                    abs(row["gasto"] - row["orig_gasto"]) > 0.01):
                                    actualizar_fila_drive(f_id, amigo, row["item"], row["chk"], row["gasto"])
                                    for t in st.session_state["todas_tareas"]:
                                        if str(t.get("id")) == str(f_id):
                                            t["item"] = row["item"].strip()
                                            t["estado"] = "1" if row["chk"] else "0"
                                            t["Gastos"] = str(row["gasto"])
                                    hubo_cambios = True
                            sincronizar_pestana_gastos_drive(st.session_state["todas_tareas"], st.session_state["amigos_pescadores"])
                            if hubo_cambios:
                                notificar(f"Se actualizaron los cambios de {amigo} correctamente.")
                            else:
                                notificar(f"No hubo cambios pendientes para guardar en {amigo}.", tipo="info")
                            st.rerun()

                    with st.expander(f"➕ Sumar ítem a {amigo}"):
                        c_an, c_ac = st.columns([3, 2])
                        with c_an: in_a_nom = st.text_input("Artículo / Tarea:", placeholder="Ej: Nafta, Carnada, Pan...", key=f"in_an_{amigo}")
                        with c_ac: in_a_cos = st.number_input("Gasto $ (0 si es solo tarea):", min_value=0.0, step=500.0, format="%.2f", key=f"in_ac_{amigo}")
                        if st.button(f"➕ Agregar a {amigo}", key=f"btn_add_p_{amigo}", use_container_width=True):
                            if in_a_nom.strip():
                                with st.spinner(f"Agregando '{in_a_nom.strip()}' a Google Drive..."):
                                    agregar_fila_drive(max_id + 1, amigo, in_a_nom.strip(), in_a_cos)
                                    st.session_state["todas_tareas"].append({
                                        "id": str(max_id + 1), "responsable": amigo, "item": in_a_nom.strip(), "estado": "0", "Gastos": str(in_a_cos)
                                    })
                                    sincronizar_pestana_gastos_drive(st.session_state["todas_tareas"], st.session_state["amigos_pescadores"])
                                    notificar(f"Se agregó '{in_a_nom.strip()}' a la lista de {amigo}.")
                                    st.rerun()

# ------------------------------------------------------------------------------
# PESTAÑA 2: CUENTAS CLARAS (FINTECH DASHBOARD)
# ------------------------------------------------------------------------------
with tab_cuentas:
    pagos_amigos = {a: 0.0 for a in amigos_pescadores}

    for t in tareas_compras:
        r = t.get("responsable", "").strip().title()
        try:
            m = float(t.get("Gastos") or t.get("gastos") or 0.0)
        except (ValueError, TypeError):
            m = 0.0

        if r in pagos_amigos:
            pagos_amigos[r] += m

    total_general = sum(pagos_amigos.values())
    cant_p = len(amigos_pescadores)
    cuota = total_general / cant_p if cant_p > 0 else 0

    st.markdown(f"""
    <div style="background: linear-gradient(135deg, #0369a1 0%, #0284c7 100%); border-radius: 20px; padding: 32px 24px; text-align: center; color: #ffffff; box-shadow: 0 8px 24px rgba(2, 132, 199, 0.2); margin-bottom: 24px;">
        <div style="font-size: 0.95rem; font-weight: 800; text-transform: uppercase; letter-spacing: 1px; color: #e0f2fe;">Gasto Total Consolidado</div>
        <div style="font-size: 3.5rem; font-weight: 900; color: #ffffff; margin: 8px 0; letter-spacing: -1px;">${total_general:,.2f}</div>
        <div style="font-size: 1.25rem; font-weight: 600; color: #e0f2fe;">
            Cuota parte individual: <span style="color: #ffffff; font-weight: 900; background: rgba(255,255,255,0.2); padding: 4px 14px; border-radius: 9999px;">${cuota:,.2f}</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 💳 Estado de Cuentas por Pescador")
    st.write("")

    for a in amigos_pescadores:
        p = pagos_amigos[a]
        dif = p - cuota
        
        if dif > 0.01:
            chip_html = f"<span class='fintech-chip chip-green'>🟢 Reintegro a favor: ${dif:,.2f}</span>"
            border_color = "#10b981"
        elif dif < -0.01:
            chip_html = f"<span class='fintech-chip chip-red'>🔴 Debe transferir: ${abs(dif):,.2f}</span>"
            border_color = "#ef4444"
        else:
            chip_html = "<span class='fintech-chip chip-gray'>⚪ Al día ($0.00)</span>"
            border_color = "#cbd5e1"

        st.markdown(f"""
        <div style="background: #ffffff; border: 1.5px solid #e2e8f0; border-left: 6px solid {border_color}; border-radius: 16px; padding: 18px 24px; margin-bottom: 14px; display: flex; justify-content: space-between; align-items: center; box-shadow: 0 2px 6px rgba(15,23,42,0.03);">
            <div>
                <div style="font-size: 1.35rem; font-weight: 800; color: #0f172a;">👤 {a}</div>
                <div style="color: #64748b; font-size: 1.05rem; margin-top: 2px;">Aporte de su bolsillo: <b>${p:,.2f}</b></div>
            </div>
            <div>
                {chip_html}
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### 🔄 Transferencias Recomendadas")
    deudores = [[a, -(pagos_amigos[a] - cuota)] for a in amigos_pescadores if (pagos_amigos[a] - cuota) < -0.01]
    acreedores = [[a, pagos_amigos[a] - cuota] for a in amigos_pescadores if (pagos_amigos[a] - cuota) > 0.01]

    if not deudores:
        st.success("🎉 ¡Todas las cuentas están saldadas o no hay gastos cargados!")
    else:
        i, j = 0, 0
        while i < len(deudores) and j < len(acreedores):
            deudor, deuda = deudores[i]
            acreedor, credito = acreedores[j]
            monto_transf = min(deuda, credito)

            st.markdown(f"""
            <div style="background-color: #f0f9ff; border: 1.5px solid #bae6fd; padding: 18px 24px; border-radius: 16px; margin-bottom: 12px; font-size: 1.25rem; color: #0369a1; display: flex; align-items: center; justify-content: space-between;">
                <div>👉 <b>{deudor}</b> le transfiere a <b>{acreedor}</b></div>
                <div style="font-size: 1.45rem; font-weight: 900; color: #0284c7;">${monto_transf:,.2f}</div>
            </div>
            """, unsafe_allow_html=True)

            deudores[i][1] -= monto_transf
            acreedores[j][1] -= monto_transf

            if deudores[i][1] < 0.01: i += 1
            if acreedores[j][1] < 0.01: j += 1

# ------------------------------------------------------------------------------
# PESTAÑA 3: RECORDATORIOS
# ------------------------------------------------------------------------------
with tab_recordatorios:
    with st.container(border=True):
        st.markdown("<div style='font-size: 1.6rem; font-weight: 900; color: #0284c7;'>🎒 Cosas para no olvidar</div>", unsafe_allow_html=True)
        st.caption("Equipo, herramientas y artículos esenciales que no implican gastos.")
        st.write("")

        cambios_rec = []
        for it in tareas_recordatorios:
            it_id = it.get("id")
            r_item = str(it.get("item", ""))
            r_chk = str(it.get("estado", "0")) == "1"

            c1, c2, c3 = st.columns([0.8, 4.4, 0.8])
            with c1: v_chk = st.checkbox("", value=r_chk, key=f"rec_c_{it_id}", label_visibility="collapsed")
            with c2: v_txt = st.text_input("Ítem", value=r_item, key=f"rec_t_{it_id}", label_visibility="collapsed")
            with c3:
                with st.popover("🗑️", help="Eliminar recordatorio"):
                    st.markdown(f"**¿Deseas eliminar '{r_item}'?**")
                    col_si, col_no = st.columns(2)
                    with col_si:
                        if st.button("Sí", key=f"del_si_rec_{it_id}", type="primary", use_container_width=True):
                            with st.spinner(f"Eliminando recordatorio de Google Drive..."):
                                borrar_fila_drive(it_id)
                                st.session_state["todas_tareas"] = [t for t in st.session_state["todas_tareas"] if str(t.get("id")) != str(it_id)]
                                notificar(f"Se eliminó el recordatorio '{r_item}'.")
                                st.rerun()
                    with col_no:
                        if st.button("No", key=f"del_no_rec_{it_id}", use_container_width=True):
                            st.rerun()

            cambios_rec.append({"id": it_id, "item": v_txt, "chk": v_chk})

        st.write("")
        if st.button("💾 Guardar estado de recordatorios", key="btn_save_rec", use_container_width=True):
            with st.spinner("Guardando recordatorios en Google Drive..."):
                for row in cambios_rec:
                    actualizar_fila_drive(row["id"], "Recordatorio", row["item"], row["chk"], 0.0)
                    for t in st.session_state["todas_tareas"]:
                        if str(t.get("id")) == str(row["id"]):
                            t["item"] = row["item"].strip()
                            t["estado"] = "1" if row["chk"] else "0"
                notificar("Se guardó el estado de los recordatorios con éxito.")
                st.rerun()

        with st.expander("➕ Sumar nuevo recordatorio"):
            in_rec = st.text_input("Nuevo recordatorio:", placeholder="Ej: Linterna frontal, repelente...", key="in_rec_val")
            if st.button("➕ Agregar recordatorio", key="btn_add_rec_val", use_container_width=True):
                if in_rec.strip():
                    with st.spinner("Guardando recordatorio en Google Drive..."):
                        agregar_fila_drive(max_id + 1, "Recordatorio", in_rec.strip(), 0.0)
                        st.session_state["todas_tareas"].append({
                            "id": str(max_id + 1), "responsable": "Recordatorio", "item": in_rec.strip(), "estado": "0", "Gastos": "0"
                        })
                        notificar(f"Se agregó el recordatorio '{in_rec.strip()}'.")
                        st.rerun()

# ------------------------------------------------------------------------------
# PESTAÑA 4: PESCADORES, LUGARES & REINICIAR
# ------------------------------------------------------------------------------
with tab_ajustes:
    with st.container(border=True):
        st.markdown("<div style='font-size: 1.6rem; font-weight: 900; color: #0284c7;'>👥 Administrar Pescadores</div>", unsafe_allow_html=True)
        st.caption("Podés reemplazar un pescador si no viaja, o quitarlo del grupo.")
        st.write("")

        for p in amigos_pescadores:
            col_p1, col_p2, col_p3 = st.columns([2.5, 1.5, 1])
            with col_p1:
                st.markdown(f"<div style='font-size: 1.25rem; font-weight: 800; color: #0f172a;'>👤 {p}</div>", unsafe_allow_html=True)
            with col_p2:
                with st.popover("✏️ Reemplazar", key=f"pop_aj_{p}", use_container_width=True):
                    nuevo_p_name = st.text_input("Reemplazar por:", value=p, key=f"in_aj_ren_{p}")
                    if st.button("Aplicar reemplazo", key=f"btn_aj_ren_{p}", use_container_width=True):
                        if nuevo_p_name.strip() and nuevo_p_name.strip().title() != p:
                            n_clean = nuevo_p_name.strip().title()
                            with st.spinner(f"Reemplazando a {p} por {n_clean} en Google Drive..."):
                                reemplazar_pescador_drive(p, n_clean)
                                st.session_state["amigos_pescadores"] = [n_clean if x == p else x for x in st.session_state["amigos_pescadores"]]
                                for t in st.session_state["todas_tareas"]:
                                    if t.get("responsable", "").strip().lower() == p.lower():
                                        t["responsable"] = n_clean
                                sincronizar_pestana_gastos_drive(st.session_state["todas_tareas"], st.session_state["amigos_pescadores"])
                                notificar(f"Se reemplazó a {p} por {n_clean} con éxito.")
                                st.rerun()
            with col_p3:
                with st.popover("Quitar", key=f"pop_del_p_{p}", use_container_width=True):
                    st.markdown(f"**¿Deseas quitar a {p}?**")
                    st.caption("Se eliminará de la lista de amigos y del Sheet.")
                    col_p_si, col_p_no = st.columns(2)
                    with col_p_si:
                        if st.button("Sí", key=f"btn_conf_del_p_{p}", type="primary", use_container_width=True):
                            with st.spinner(f"Quitando a {p} de Google Drive..."):
                                borrar_pescador_drive(p)
                                st.session_state["amigos_pescadores"] = [x for x in st.session_state["amigos_pescadores"] if x != p]
                                notificar(f"Se quitó a {p} del grupo.")
                                st.rerun()
                    with col_p_no:
                        if st.button("No", key=f"btn_canc_del_p_{p}", use_container_width=True):
                            st.rerun()

        st.write("")
        with st.form(key="form_nuevo_amigo", clear_on_submit=True):
            nuevo_amigo_txt = st.text_input("Nombre de nuevo pescador:")
            if st.form_submit_button("➕ Sumar nuevo pescador", use_container_width=True):
                if nuevo_amigo_txt.strip():
                    n_p_clean = nuevo_amigo_txt.strip().title()
                    with st.spinner(f"Sumando a {n_p_clean} en Google Drive..."):
                        agregar_pescador_drive(n_p_clean)
                        st.session_state["amigos_pescadores"].append(n_p_clean)
                        notificar(f"Se sumó a {n_p_clean} al grupo.")
                        st.rerun()

        st.markdown("---")
        st.markdown("<div style='font-size: 1.4rem; font-weight: 800; color: #0284c7;'>🏪 Lugares de Compra Externos</div>", unsafe_allow_html=True)
        for lug in lugares_detectados:
            st.markdown(f"- 🏪 **{lug}**")

        with st.form(key="form_nuevo_lugar", clear_on_submit=True):
            nuevo_lugar_txt = st.text_input("Nombre del nuevo lugar (Ej: Carnada Km 45, Estación YPF):")
            if st.form_submit_button("➕ Agregar nuevo lugar", use_container_width=True):
                if nuevo_lugar_txt.strip():
                    n_l_clean = nuevo_lugar_txt.strip()
                    with st.spinner(f"Creando '{n_l_clean}' en Google Drive..."):
                        agregar_fila_drive(max_id + 1, n_l_clean, "Primer ítem de compra", 0.0)
                        st.session_state["todas_tareas"].append({
                            "id": str(max_id + 1), "responsable": n_l_clean, "item": "Primer ítem de compra", "estado": "0", "Gastos": "0"
                        })
                        notificar(f"Se creó el lugar '{n_l_clean}' con éxito.")
                        st.rerun()

        st.markdown("---")
        st.markdown("<div style='font-size: 1.4rem; font-weight: 800; color: #ef4444;'>⚠️ Reiniciar Salida para un Nuevo Viaje</div>", unsafe_allow_html=True)
        st.caption("Destilda todos los artículos y pone los gastos en $0 sin borrar tus listas ni los amigos.")
        chk_reset = st.checkbox("Confirmo reiniciar todos los gastos y tareas a cero.")
        if st.button("🔄 Reiniciar Salida Completa", disabled=not chk_reset, use_container_width=True):
            with st.spinner("Reiniciando salida a $0 en Google Drive..."):
                reiniciar_salida_drive(st.session_state["todas_tareas"], st.session_state["amigos_pescadores"])
                for t in st.session_state["todas_tareas"]:
                    t["estado"] = "0"
                    t["Gastos"] = "0"
                sincronizar_pestana_gastos_drive(st.session_state["todas_tareas"], st.session_state["amigos_pescadores"])
                notificar("Salida reiniciada a cero para el próximo viaje.")
                st.rerun()