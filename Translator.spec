# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['Translator.py','mcstructureTojson.py','function.py','__init__.py','share.py','./blockData/__init__.py','./blockData/blockList.py','./blockData/fence_gate.py','./blockData/stairs.py','./blockData/door.py','./blockData/ladder.py','./blockData/slab.py','./blockData/prismarine.py','./blockData/stonebrick.py','./blockData/stained_glass.py','./blockData/sandstone.py','./blockData/quartz_block.py','./blockData/bed.py','./blockData/candle.py','./blockData/campfire.py','./blockData/furnace.py','./blockData/respawn_anchor.py','./blockData/anvil.py','./blockData/standing_sign.py','./blockData/torch.py','./blockData/grindstone.py','./blockData/cauldron.py','./blockData/composter.py','./blockData/end_portal_frame.py','./blockData/light_block.py','./blockData/rail.py','./blockData/sea_pickle.py','./blockData/lever.py','./blockData/tripwire_hook.py','./blockData/unpowered_repeater.py','./blockData/unpowered_comparator.py','./blockData/farmland.py','./blockData/log.py','./blockData/wood.py','./blockData/leaves.py','./blockData/sapling.py','./blockData/wheat.py','./blockData/tallgrass.py','./blockData/double_plant.py','./blockData/coral.py','./blockData/kelp.py','./blockData/red_flower.py','./blockData/cocoa.py','./blockData/vine.py','./blockData/twisting_vines.py','./blockData/bamboo.py','./blockData/snow_layer.py','./blockData/glow_lichen.py','./blockData/brown_mushroom_block.py','./blockData/reeds.py','./blockData/turtle_egg.py','./blockData/sponge.py','./blockData/water.py','./blockData/stone.py','./blockData/planks.py'],
    pathex=['E:/Happy2018newの个人文件/Create/正在支持的开发项目/结构翻译器/开发/'],
    binaries=[],
    datas=[],
    hiddenimports=['blockData.planks','blockData.stone','blockData.water','blockData.sponge','blockData.turtle_egg','blockData.reeds','blockData.brown_mushroom_block','blockData.glow_lichen','blockData.snow_layer','blockData.bamboo','blockData.twisting_vines','blockData.vine','blockData.cocoa','blockData.red_flower','blockData.kelp','blockData.coral','blockData.double_plant','blockData.tallgrass','blockData.wheat','blockData.sapling','blockData.leaves','blockData.wood','blockData.log','blockData.farmland','blockData.unpowered_comparator','blockData.unpowered_repeater','blockData.tripwire_hook','blockData.lever','blockData.sea_pickle','blockData.rail','blockData.light_block','blockData.end_portal_frame','blockData.composter','blockData.cauldron','blockData.grindstone','blockData.torch','blockData.standing_sign','blockData.anvil','blockData.respawn_anchor','blockData.furnace','blockData.campfire','blockData.candle','blockData.bed','blockData.quartz_block','blockData.sandstone','blockData.stained_glass','blockData.stonebrick','blockData.prismarine','blockData.slab','blockData.ladder','blockData.door','blockData.fence_gate','blockData.stairs','blockData.blockList'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='Translator',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
