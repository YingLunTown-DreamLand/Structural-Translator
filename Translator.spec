# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['Translator.py','startFunction.py','pool.py','check.py','mcstructureTojson.py','function.py','__init__.py','share.py','./blockData/__init__.py','./blockData/blockList.py','./blockData/fence_gate.py','./blockData/stairs.py','./blockData/door.py','./blockData/slab.py','./blockData/prismarine.py','./blockData/stonebrick.py','./blockData/stained_glass.py','./blockData/sandstone.py','./blockData/quartz_block.py','./blockData/bed.py','./blockData/candle.py','./blockData/campfire.py','./blockData/furnace.py','./blockData/respawn_anchor.py','./blockData/anvil.py','./blockData/standing_sign.py','./blockData/torch.py','./blockData/grindstone.py','./blockData/cauldron.py','./blockData/composter.py','./blockData/end_portal_frame.py','./blockData/light_block.py','./blockData/rail.py','./blockData/sea_pickle.py','./blockData/lever.py','./blockData/tripwire_hook.py','./blockData/unpowered_repeater.py','./blockData/unpowered_comparator.py','./blockData/farmland.py','./blockData/log.py','./blockData/wood.py','./blockData/leaves.py','./blockData/sapling.py','./blockData/wheat.py','./blockData/tallgrass.py','./blockData/double_plant.py','./blockData/coral.py','./blockData/kelp.py','./blockData/red_flower.py','./blockData/cocoa.py','./blockData/vine.py','./blockData/twisting_vines.py','./blockData/bamboo.py','./blockData/snow_layer.py','./blockData/glow_lichen.py','./blockData/brown_mushroom_block.py','./blockData/reeds.py','./blockData/turtle_egg.py','./blockData/sponge.py','./blockData/water.py','./blockData/stone.py','./blockData/planks.py',
'./Others/TranslateJSON.py','./Others/__init__.py','./blockData/dirt.py','./blockData/bedrock.py',
'./blockData/cobblestone_wall.py','./blockData/lantern.py','./blockData/fence.py','./blockData/chain.py',
'./blockData/monster_egg.py','./blockData/sand.py','./blockData/portal.py',
'./blockNBT/CommandBlock.py','./blockNBT/main.py','./blockNBT/Container.py',
'./blockNBT/__init__.py','./Others/CommandBlock.py','./Others/NBTtranslate.py',
'./Others/Synthetic.py','./Api/JsonToNBT/JsonTranslate.py','./ACME/TranslateMCACBLOCK.py',
'./blockData_NoType/__init__.py','./blockData_NoType/fence_gate.py','./blockData_NoType/stairs.py','./blockData_NoType/door.py','./blockData_NoType/slab.py','./blockData_NoType/prismarine.py','./blockData_NoType/stonebrick.py','./blockData_NoType/stained_glass.py','./blockData_NoType/sandstone.py','./blockData_NoType/quartz_block.py','./blockData_NoType/bed.py','./blockData_NoType/candle.py','./blockData_NoType/campfire.py','./blockData_NoType/furnace.py','./blockData_NoType/respawn_anchor.py','./blockData_NoType/anvil.py','./blockData_NoType/standing_sign.py','./blockData_NoType/torch.py','./blockData_NoType/grindstone.py','./blockData_NoType/cauldron.py','./blockData_NoType/composter.py','./blockData_NoType/end_portal_frame.py','./blockData_NoType/light_block.py','./blockData_NoType/rail.py','./blockData_NoType/sea_pickle.py','./blockData_NoType/lever.py','./blockData_NoType/tripwire_hook.py','./blockData_NoType/unpowered_repeater.py','./blockData_NoType/unpowered_comparator.py','./blockData_NoType/farmland.py','./blockData_NoType/log.py','./blockData_NoType/wood.py','./blockData_NoType/leaves.py','./blockData_NoType/sapling.py','./blockData_NoType/wheat.py','./blockData_NoType/tallgrass.py','./blockData_NoType/double_plant.py','./blockData_NoType/coral.py','./blockData_NoType/kelp.py','./blockData_NoType/red_flower.py','./blockData_NoType/cocoa.py','./blockData_NoType/vine.py','./blockData_NoType/twisting_vines.py','./blockData_NoType/bamboo.py','./blockData_NoType/snow_layer.py','./blockData_NoType/glow_lichen.py','./blockData_NoType/brown_mushroom_block.py','./blockData_NoType/reeds.py','./blockData_NoType/turtle_egg.py','./blockData_NoType/sponge.py','./blockData_NoType/water.py','./blockData_NoType/stone.py','./blockData_NoType/planks.py',
'./Others/TranslateJSON.py','./Others/__init__.py','./blockData_NoType/dirt.py','./blockData_NoType/bedrock.py',
'./blockData_NoType/cobblestone_wall.py','./blockData_NoType/lantern.py','./blockData_NoType/fence.py','./blockData_NoType/chain.py',
'./blockData_NoType/monster_egg.py','./blockData_NoType/sand.py','./blockData_NoType/portal.py'],
    pathex=['E:/Happy2018newの个人文件/GitHub/Structural-Translator/'],
    binaries=[],
    datas=[],
    hiddenimports=['ACME.TranslateMCACBLOCK','Api.JsonToNBT.JsonTranslate','Others.Synthetic','Others.NBTtranslate','Others.CommandBlock','blockNBT.Container','blockNBT.CommandBlock','blockNBT.main','blockData.portal','Others.TranslateJSON','blockData.sand','blockData.monster_egg','blockData.chain','blockData.fence','blockData.lantern','blockData.cobblestone_wall','blockData.bedrock','blockData.dirt','Others.TranslateJSON','blockData.planks','blockData.stone','blockData.water','blockData.sponge','blockData.turtle_egg','blockData.reeds','blockData.brown_mushroom_block','blockData.glow_lichen','blockData.snow_layer','blockData.bamboo','blockData.twisting_vines','blockData.vine','blockData.cocoa','blockData.red_flower','blockData.kelp','blockData.coral','blockData.double_plant','blockData.tallgrass','blockData.wheat','blockData.sapling','blockData.leaves','blockData.wood','blockData.log','blockData.farmland','blockData.unpowered_comparator','blockData.unpowered_repeater','blockData.tripwire_hook','blockData.lever','blockData.sea_pickle','blockData.rail','blockData.light_block','blockData.end_portal_frame','blockData.composter','blockData.cauldron','blockData.grindstone','blockData.torch','blockData.standing_sign','blockData.anvil','blockData.respawn_anchor','blockData.furnace','blockData.campfire','blockData.candle','blockData.bed','blockData.quartz_block','blockData.sandstone','blockData.stained_glass','blockData.stonebrick','blockData.prismarine','blockData.slab','blockData.door','blockData.fence_gate','blockData.stairs','blockData.blockList','blockData_NoType.portal', 'blockData_NoType.sand', 'blockData_NoType.monster_egg', 'blockData_NoType.chain', 'blockData_NoType.fence', 'blockData_NoType.lantern', 'blockData_NoType.cobblestone_wall', 'blockData_NoType.bedrock', 'blockData_NoType.dirt', 'blockData_NoType.planks', 'blockData_NoType.stone', 'blockData_NoType.water', 'blockData_NoType.sponge', 'blockData_NoType.turtle_egg', 'blockData_NoType.reeds', 'blockData_NoType.brown_mushroom_block', 'blockData_NoType.glow_lichen', 'blockData_NoType.snow_layer', 'blockData_NoType.bamboo', 'blockData_NoType.twisting_vines', 'blockData_NoType.vine', 'blockData_NoType.cocoa', 'blockData_NoType.red_flower', 'blockData_NoType.kelp', 'blockData_NoType.coral', 'blockData_NoType.double_plant', 'blockData_NoType.tallgrass', 'blockData_NoType.wheat', 'blockData_NoType.sapling', 'blockData_NoType.leaves', 'blockData_NoType.wood', 'blockData_NoType.log', 'blockData_NoType.farmland', 'blockData_NoType.unpowered_comparator', 'blockData_NoType.unpowered_repeater', 'blockData_NoType.tripwire_hook', 'blockData_NoType.lever', 'blockData_NoType.sea_pickle', 'blockData_NoType.rail', 'blockData_NoType.light_block', 'blockData_NoType.end_portal_frame', 'blockData_NoType.composter', 'blockData_NoType.cauldron', 'blockData_NoType.grindstone', 'blockData_NoType.torch', 'blockData_NoType.standing_sign', 'blockData_NoType.anvil', 'blockData_NoType.respawn_anchor', 'blockData_NoType.furnace', 'blockData_NoType.campfire', 'blockData_NoType.candle', 'blockData_NoType.bed', 'blockData_NoType.quartz_block', 'blockData_NoType.sandstone', 'blockData_NoType.stained_glass', 'blockData_NoType.stonebrick', 'blockData_NoType.prismarine', 'blockData_NoType.slab', 'blockData_NoType.door', 'blockData_NoType.fence_gate', 'blockData_NoType.stairs'],
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
